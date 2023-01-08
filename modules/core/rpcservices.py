import udaconnect_pb2
import udaconnect_pb2_grpc
from app import app
from services import PersonService


class PersonServicer(udaconnect_pb2_grpc.PersonServicer):

    def Get(self, request, context):
        with app.app_context():
            person = PersonService.retrieve(request.id)
            return udaconnect_pb2.GetPersonResponse(
                data=udaconnect_pb2.PersonMessage(
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
            return udaconnect_pb2.CreatePersonResponse(
                data=udaconnect_pb2.PersonMessage(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name,
                )
            )

    def GetAll(self, request, context):
        with app.app_context():
            person_list = PersonService.retrieve_all()
            person_proto_list = list(
                map(lambda person: udaconnect_pb2.PersonMessage(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name,
                ), person_list)
            )
            return udaconnect_pb2.GetAllPersonResponse(list=person_proto_list)
