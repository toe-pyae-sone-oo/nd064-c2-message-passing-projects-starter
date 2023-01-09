import grpc
import udaconnect_pb2
import udaconnect_pb2_grpc

channel = grpc.insecure_channel("localhost:30002")
stub = udaconnect_pb2_grpc.LocationStub(channel)

response = stub.AsyncCreate(udaconnect_pb2.AsyncCreateLocationRequest(
    payload=udaconnect_pb2.LocationMessage(
        person_id=5,
        longitude="37.553634",
        latitude="-122.290883",
        creation_time=1673194004,
    ),
))

print(response)