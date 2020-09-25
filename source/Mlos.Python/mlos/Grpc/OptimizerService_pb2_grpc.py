# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from mlos.Grpc import OptimizerService_pb2 as mlos_dot_Grpc_dot_OptimizerService__pb2


class OptimizerServiceStub(object):
    """Exposes Bayesian Optimizer's functionality over gRPC.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListExistingOptimizers = channel.unary_unary(
                '/OptimizerService/ListExistingOptimizers',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerList.FromString,
                )
        self.GetOptimizerInfo = channel.unary_unary(
                '/OptimizerService/GetOptimizerInfo',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerInfo.FromString,
                )
        self.GetOptimizerConvergenceState = channel.unary_unary(
                '/OptimizerService/GetOptimizerConvergenceState',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerConvergenceState.FromString,
                )
        self.CreateOptimizer = channel.unary_unary(
                '/OptimizerService/CreateOptimizer',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.CreateOptimizerRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
                )
        self.Suggest = channel.unary_unary(
                '/OptimizerService/Suggest',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.SuggestRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.ConfigurationParameters.FromString,
                )
        self.Predict = channel.unary_unary(
                '/OptimizerService/Predict',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.PredictRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.PredictResponse.FromString,
                )
        self.RegisterObservation = channel.unary_unary(
                '/OptimizerService/RegisterObservation',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                )
        self.RegisterObservations = channel.unary_unary(
                '/OptimizerService/RegisterObservations',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationsRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                )
        self.GetAllObservations = channel.unary_unary(
                '/OptimizerService/GetAllObservations',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Observations.FromString,
                )


class OptimizerServiceServicer(object):
    """Exposes Bayesian Optimizer's functionality over gRPC.

    """

    def ListExistingOptimizers(self, request, context):
        """Returns a list of existing optimizer instances.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOptimizerInfo(self, request, context):
        """Returns information about optimizers configuration and optimization problem.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOptimizerConvergenceState(self, request, context):
        """Returns the current optimizer convergence state.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOptimizer(self, request, context):
        """Creates an optimizer with the specified configuration.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Suggest(self, request, context):
        """Request a suggestion.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Predict(self, request, context):
        """Produces a prediction for specified features.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterObservation(self, request, context):
        """Adds an observation to the optimizer's data set.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterObservations(self, request, context):
        """Adds observations to the optimizer's data set.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllObservations(self, request, context):
        """Returns all observations registered for a given optimizer.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OptimizerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListExistingOptimizers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExistingOptimizers,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerList.SerializeToString,
            ),
            'GetOptimizerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOptimizerInfo,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerInfo.SerializeToString,
            ),
            'GetOptimizerConvergenceState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOptimizerConvergenceState,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerConvergenceState.SerializeToString,
            ),
            'CreateOptimizer': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOptimizer,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.CreateOptimizerRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
            ),
            'Suggest': grpc.unary_unary_rpc_method_handler(
                    servicer.Suggest,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.SuggestRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.ConfigurationParameters.SerializeToString,
            ),
            'Predict': grpc.unary_unary_rpc_method_handler(
                    servicer.Predict,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.PredictRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.PredictResponse.SerializeToString,
            ),
            'RegisterObservation': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterObservation,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
            ),
            'RegisterObservations': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterObservations,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationsRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
            ),
            'GetAllObservations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllObservations,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Observations.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OptimizerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OptimizerService(object):
    """Exposes Bayesian Optimizer's functionality over gRPC.

    """

    @staticmethod
    def ListExistingOptimizers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/ListExistingOptimizers',
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOptimizerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/GetOptimizerInfo',
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOptimizerConvergenceState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/GetOptimizerConvergenceState',
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerConvergenceState.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOptimizer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/CreateOptimizer',
            mlos_dot_Grpc_dot_OptimizerService__pb2.CreateOptimizerRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Suggest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/Suggest',
            mlos_dot_Grpc_dot_OptimizerService__pb2.SuggestRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.ConfigurationParameters.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/Predict',
            mlos_dot_Grpc_dot_OptimizerService__pb2.PredictRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.PredictResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterObservation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/RegisterObservation',
            mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterObservations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/RegisterObservations',
            mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationsRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllObservations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OptimizerService/GetAllObservations',
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.Observations.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
