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