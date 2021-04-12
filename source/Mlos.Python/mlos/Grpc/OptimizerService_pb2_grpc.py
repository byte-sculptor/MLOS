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
        self.CreateOptimizer = channel.unary_unary(
                '/mlos.optimizer_service.OptimizerService/CreateOptimizer',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.CreateOptimizerRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
                )
        self.GetOptimizerInfo = channel.unary_unary(
                '/mlos.optimizer_service.OptimizerService/GetOptimizerInfo',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerInfo.FromString,
                )
        self.Suggest = channel.unary_unary(
                '/mlos.optimizer_service.OptimizerService/Suggest',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.SuggestRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.ConfigurationParameters.FromString,
                )
        self.RegisterObservation = channel.unary_unary(
                '/mlos.optimizer_service.OptimizerService/RegisterObservation',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                )
        self.RegisterObservations = channel.unary_unary(
                '/mlos.optimizer_service.OptimizerService/RegisterObservations',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationsRequest.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                )
        self.Echo = channel.unary_unary(
                '/mlos.optimizer_service.OptimizerService/Echo',
                request_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
                response_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                )


class OptimizerServiceServicer(object):
    """Exposes Bayesian Optimizer's functionality over gRPC.

    """

    def CreateOptimizer(self, request, context):
        """Creates an optimizer with the specified configuration.

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

    def Suggest(self, request, context):
        """Request a suggestion.

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

    def Echo(self, request, context):
        """Like ping.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OptimizerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOptimizer': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOptimizer,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.CreateOptimizerRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
            ),
            'GetOptimizerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOptimizerInfo,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerInfo.SerializeToString,
            ),
            'Suggest': grpc.unary_unary_rpc_method_handler(
                    servicer.Suggest,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.SuggestRequest.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.ConfigurationParameters.SerializeToString,
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
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
                    response_serializer=mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mlos.optimizer_service.OptimizerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OptimizerService(object):
    """Exposes Bayesian Optimizer's functionality over gRPC.

    """

    @staticmethod
    def CreateOptimizer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mlos.optimizer_service.OptimizerService/CreateOptimizer',
            mlos_dot_Grpc_dot_OptimizerService__pb2.CreateOptimizerRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOptimizerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mlos.optimizer_service.OptimizerService/GetOptimizerInfo',
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerHandle.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.OptimizerInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Suggest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mlos.optimizer_service.OptimizerService/Suggest',
            mlos_dot_Grpc_dot_OptimizerService__pb2.SuggestRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.ConfigurationParameters.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterObservation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mlos.optimizer_service.OptimizerService/RegisterObservation',
            mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterObservations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mlos.optimizer_service.OptimizerService/RegisterObservations',
            mlos_dot_Grpc_dot_OptimizerService__pb2.RegisterObservationsRequest.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mlos.optimizer_service.OptimizerService/Echo',
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.SerializeToString,
            mlos_dot_Grpc_dot_OptimizerService__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
