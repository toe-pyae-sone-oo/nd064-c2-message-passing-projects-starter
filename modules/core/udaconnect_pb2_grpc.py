# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import udaconnect_pb2 as udaconnect__pb2


class PersonStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/Person/Get',
                request_serializer=udaconnect__pb2.GetPersonRequest.SerializeToString,
                response_deserializer=udaconnect__pb2.GetPersonResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/Person/Create',
                request_serializer=udaconnect__pb2.CreatePersonRequest.SerializeToString,
                response_deserializer=udaconnect__pb2.CreatePersonResponse.FromString,
                )
        self.GetAll = channel.unary_unary(
                '/Person/GetAll',
                request_serializer=udaconnect__pb2.GetAllPersonRequest.SerializeToString,
                response_deserializer=udaconnect__pb2.GetAllPersonResponse.FromString,
                )


class PersonServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=udaconnect__pb2.GetPersonRequest.FromString,
                    response_serializer=udaconnect__pb2.GetPersonResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=udaconnect__pb2.CreatePersonRequest.FromString,
                    response_serializer=udaconnect__pb2.CreatePersonResponse.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=udaconnect__pb2.GetAllPersonRequest.FromString,
                    response_serializer=udaconnect__pb2.GetAllPersonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Person', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Person(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Person/Get',
            udaconnect__pb2.GetPersonRequest.SerializeToString,
            udaconnect__pb2.GetPersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Person/Create',
            udaconnect__pb2.CreatePersonRequest.SerializeToString,
            udaconnect__pb2.CreatePersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Person/GetAll',
            udaconnect__pb2.GetAllPersonRequest.SerializeToString,
            udaconnect__pb2.GetAllPersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LocationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/Location/Get',
                request_serializer=udaconnect__pb2.GetLocationRequest.SerializeToString,
                response_deserializer=udaconnect__pb2.GetLocationResponse.FromString,
                )


class LocationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=udaconnect__pb2.GetLocationRequest.FromString,
                    response_serializer=udaconnect__pb2.GetLocationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Location', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Location(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Location/Get',
            udaconnect__pb2.GetLocationRequest.SerializeToString,
            udaconnect__pb2.GetLocationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ConnectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindContacts = channel.unary_unary(
                '/Connection/FindContacts',
                request_serializer=udaconnect__pb2.FindContactsRequest.SerializeToString,
                response_deserializer=udaconnect__pb2.FindContactsResponse.FromString,
                )


class ConnectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindContacts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindContacts': grpc.unary_unary_rpc_method_handler(
                    servicer.FindContacts,
                    request_deserializer=udaconnect__pb2.FindContactsRequest.FromString,
                    response_serializer=udaconnect__pb2.FindContactsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Connection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Connection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindContacts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Connection/FindContacts',
            udaconnect__pb2.FindContactsRequest.SerializeToString,
            udaconnect__pb2.FindContactsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
