#
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
#
from functools import wraps
from multiprocessing import Queue, Event
from multiprocessing.shared_memory import SharedMemory
import os
import pickle
from queue import Empty
from typing import Dict
import time

from mlos.DataPlane.ModelHosting.ModelHostMessages import Response, PredictRequest, PredictResponse, TrainRequest, TrainResponse
from mlos.DataPlane.SharedMemoryDataSetView import attached_data_set_view
from mlos.Logger import create_logger
from mlos.Optimizers.RegressionModels.RegressionModel import RegressionModel

def request_handler():
    def request_handler_decorator(wrapped_function):
        @wraps(wrapped_function)
        def wrapper(*args, **kwargs):
            try:
                request_id = None
                request = kwargs['request']
                request_id = request.request_id

                return wrapped_function(*args, **kwargs)
            except Exception as e:
                self = args[0]
                self.logger.error(f"Failed to process request:  {request_id}", exc_info=True)
                return Response(request_id=request_id, success=False, exception=e)

        return wrapper
    return request_handler_decorator


class SharedMemoryModelHost:
    """A worker responsible for scoring models held in shared memory.

    Objective:
        The goal is to parallelize model scoring (calls to model.predict(...)) so as to have many trees evaluating simultaneously
        in shared memory. This should provide a considerable speed boost for producing suggestions, tomograph interactions, and
        lastly model training.


    Strategy:
        Each instance of shared memory model executor will listen for requests on a queue. Once a request object is received,
        the executor will check its cache to see if it already has the requisite model deserialized, if it doesn't, it will locate
        the model in shared memory and deserialize it.

        It will then locate the features_df in shared memory and invoke the model's predict() method. Lastly, it will stash the
        prediction's dataframe in shared memory and send back the message informing the client how to find it.

        Finally, once all of the above works, we can extend the Host to also fit the models and place them in shared memory.


    Additional Notes:
        Tracing shows that currently, serial execution of models is one of the biggest bottlenecks in both registering an observation,
        and - more importantly - producing a suggestion. Parallelizing inference is the single biggest low-hanging fruit we have.

        Since Python is not big on multi-threading (GIL is here to stay), the preferred parallelization method is to use multiple
        processes. This creates the question of inter-process communication. We have a ton of options:
            * shared memory
            * pipes
            * sockets
            * ...
        But only shared memory lets us avoid unnecessary copying and serializing/deserializing of our (relatively large) dataframes
        and models. So we will leverage Python's multiprocessing.SharedMemory module to stash our data and models in shared memory.

    """

    def __init__(
        self,
        request_queue: Queue,
        response_queue: Queue,
        shutdown_event: Event,
        logger = None
    ):
        if logger is None:
            logger = create_logger(self.__class__.__name__)
        self.logger = logger
        self.request_queue: Queue = request_queue
        self.response_queue: Queue = response_queue
        self.shutdown_event: Event = shutdown_event
        self._model_cache: Dict[str, RegressionModel] = dict()

        # We need to keep a reference to SharedMemory objects, or they will be garbage collected.
        #
        self._shared_memory_cache: Dict[str, SharedMemory] = dict()

    def run(self):
        self.logger.info(f'{os.getpid()} running')
        timeout_s = 1
        while not self.shutdown_event.is_set():
            try:
                request = self.request_queue.get(block=True, timeout=timeout_s)
                self.logger.info(f"{os.getpid()} Got request of type: {type(request)}")
            except Empty:
                continue

            if isinstance(request, PredictRequest):
                response = self._process_predict_request(request=request)
            elif isinstance(request, TrainRequest):
                response = self._process_train_request(request=request)
            else:
                response = Response(
                    request_id=request.request_id,
                    success=False,
                    exception=RuntimeError(f"Unknown request type: {type(request)}")
                )
            self.response_queue.put(response)

        self.logger.info(f"{os.getpid()} shutting down")

    @request_handler()
    def _process_predict_request(self, request: PredictRequest):
        if request.model_id in self._model_cache:
            self.logger.info(f"{os.getpid()} Model id: {request.model_id} found in cache.")
            model = self._model_cache[request.model_id]
        else:
            self.logger.info(f"{os.getpid()} Model id: {request.model_id} not found in cache. Deserializing from shared memory.")
            model_shared_memory = SharedMemory(name=request.model_id, create=False)
            model = pickle.loads(model_shared_memory.buf)
            assert isinstance(model, RegressionModel)
            self._model_cache[request.model_id] = model
            model_shared_memory.close()
            self.logger.info(f"{os.getpid()} Model id: {request.model_id} deserialized from shared memory and placed in the cache.")


        with attached_data_set_view(data_set_info=request.data_set_info) as features_data_set_view:
            features_df = features_data_set_view.get_dataframe()
            prediction = model.predict(feature_values_pandas_frame=features_df, include_only_valid_rows=True)

            # TODO: put predictions in shared memory and send the response.
            response = PredictResponse(
                request_id=request.request_id,
                prediction=prediction
            )
            self.logger.info(f"{os.getpid()} Produced a response with {len(prediction.get_dataframe().index)} predictions.")
            return response


    @request_handler()
    def _process_train_request(self, request: TrainRequest):
        self.logger.info(f"Deserializing model: {request.untrained_model_id} from shared memory.")
        untrained_model_shared_memory = SharedMemory(name=request.untrained_model_id, create=False)
        model = pickle.loads(untrained_model_shared_memory.buf)
        untrained_model_shared_memory.close()
        assert isinstance(model, RegressionModel)
        self.logger.info(f"Successlly deserialized model: {request.untrained_model_id} from shared memory.")

        with attached_data_set_view(data_set_info=request.features_data_set_info) as features_data_set_view, \
            attached_data_set_view(data_set_info=request.objectives_data_set_info) as objectives_data_set_view:

            features_df = features_data_set_view.get_dataframe()
            objectives_df = objectives_data_set_view.get_dataframe()

            model.fit(
                feature_values_pandas_frame=features_df,
                target_values_pandas_frame=objectives_df,
                iteration_number=request.iteration_number
            )

            trained_model_id = f"{request.untrained_model_id}_{request.iteration_number}"
            self.logger.info(f"{os.getpid()} Successfully trained the model {trained_model_id}. Placing it in local cache and in shared memory.")

            pickled_model = pickle.dumps(model)
            trained_model_shared_memory = SharedMemory(name=trained_model_id, create=True, size=len(pickled_model))
            trained_model_shared_memory.buf[:] = pickled_model

            unpickled_model = pickle.loads(trained_model_shared_memory.buf)
            assert isinstance(unpickled_model, type(model))

            self._model_cache[trained_model_id] = model
            self._shared_memory_cache[trained_model_id] = trained_model_shared_memory

            response = TrainResponse(
                trained_model_id=trained_model_id,
                request_id=request.request_id
            )

            self.logger.info(f"{os.getpid()} Produced a response to request: {request.request_id}.")
            return response


def start_shared_memory_model_host(request_queue: Queue, response_queue: Queue, shutdown_event: Event):
    model_host = SharedMemoryModelHost(request_queue=request_queue, response_queue=response_queue, shutdown_event=shutdown_event)
    model_host.run()
