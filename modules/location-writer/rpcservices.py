from udaconnect_pb2 import CreateLocationResponse
import udaconnect_pb2_grpc
from services import (
    LocationService,
)

class LocationServicer(udaconnect_pb2_grpc.LocationServicer):

    def Create(self, request, context):
        LocationService.create({
            "person_id": request.payload.person_id,
            "creation_time": request.payload.creation_time,
            "latitude": request.payload.latitude,
            "longitude": request.payload.longitude,
        })
        return CreateLocationResponse()
