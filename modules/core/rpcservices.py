from udaconnect_pb2 import (
    PersonMessage,
    GetPersonResponse,
    CreatePersonResponse,
    GetAllPersonResponse,
    LocationMessage,
    GetLocationResponse,
)
import udaconnect_pb2_grpc
from app import app
from services import (
    PersonService,
    LocationService,
)


class PersonServicer(udaconnect_pb2_grpc.PersonServicer):

    def Get(self, request, context):
        with app.app_context():
            person = PersonService.retrieve(request.id)
            return GetPersonResponse(
                data=PersonMessage(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name,
                )
            )

    def Create(self, request, context):
        with app.app_context():
            request_payload = {
                "first_name": request.payload.first_name,
                "last_name": request.payload.last_name,
                "company_name": request.payload.company_name,
            }
            person = PersonService.create(request_payload)
            return CreatePersonResponse(
                data=PersonMessage(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name,
                )
            )

    def GetAll(self, request, context):
        with app.app_context():
            person_list = PersonService.retrieve_all()
            person_message_list = list(
                map(lambda person: PersonMessage(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name,
                ), person_list)
            )
            return GetAllPersonResponse(list=person_message_list)

class LocationServicer(udaconnect_pb2_grpc.LocationServicer):
    
    def Get(self, request, context):
        with app.app_context():
            location = LocationService.retrieve(request.id)
            return GetLocationResponse(
                data=LocationMessage(
                    id=location.id,
                    person_id=location.person_id,
                    longitude=location.longitude,
                    latitude=location.latitude,
                    creation_time=int(location.creation_time.timestamp())
                )
            )
