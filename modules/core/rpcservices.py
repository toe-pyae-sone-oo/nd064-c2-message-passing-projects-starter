from udaconnect_pb2 import (
    PersonMessage,
    GetPersonResponse,
    CreatePersonResponse,
    GetAllPersonResponse,
    LocationMessage,
    GetLocationResponse,
    CreateLocationResponse,
    ConnectionMessage,
    FindContactsResponse,
    AsyncCreateLocationResponse,
)
import udaconnect_pb2_grpc
from app import app
from services import (
    PersonService,
    LocationService,
    ConnectionService,
)
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"

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

    def Create(self, request, context):
        with app.app_context():
            location = LocationService.create({
                "person_id": request.payload.person_id,
                "creation_time": datetime.fromtimestamp(request.payload.creation_time),
                "latitude": request.payload.latitude,
                "longitude": request.payload.longitude,
            })
            return CreateLocationResponse(
                data=LocationMessage(
                    id=location.id,
                    person_id=location.person_id,
                    longitude=location.longitude,
                    latitude=location.latitude,
                    creation_time=int(location.creation_time.timestamp())
                )
            )

    def AsyncCreate(self, request, context):
        with app.app_context():
            LocationService.async_create({
                "person_id": request.payload.person_id,
                "creation_time": request.payload.creation_time,
                "latitude": request.payload.latitude,
                "longitude": request.payload.longitude,
            })
            return AsyncCreateLocationResponse()

class ConnectionServicer(udaconnect_pb2_grpc.ConnectionServicer):

    def FindContacts(self, request, context):
        start_date = datetime.strptime(request.start_date, DATE_FORMAT)
        end_date = datetime.strptime(request.end_date, DATE_FORMAT)

        with app.app_context():
            contacts = ConnectionService.find_contacts(
                request.person_id,
                start_date,
                end_date,
                request.distance,
            )

            connection_messages = list(map(lambda contact: ConnectionMessage(
                location=LocationMessage(
                    id=contact.location.id,
                    person_id=contact.location.person_id,
                    longitude=contact.location.longitude,
                    latitude=contact.location.latitude,
                    creation_time=int(contact.location.creation_time.timestamp())
                ),
                person=PersonMessage(
                    id=contact.person.id,
                    first_name=contact.person.first_name,
                    last_name=contact.person.last_name,
                    company_name=contact.person.company_name,
                ),
            ), contacts))

            return FindContactsResponse(contacts=connection_messages)