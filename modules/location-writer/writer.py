import grpc
from udaconnect_pb2 import (
    CreateLocationRequest,
    LocationMessage,
)
from udaconnect_pb2_grpc import (
    LocationStub,
)

channel = grpc.insecure_channel("localhost:30002")

location_stub = LocationStub(channel)

location_stub.Create(CreateLocationRequest(
    payload=LocationMessage(
        person_id=6,
        creation_time=1674142357,
        latitude="-122.290883",
        longitude="37.55363",
    )
))