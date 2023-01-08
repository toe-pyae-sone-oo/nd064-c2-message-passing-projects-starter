import logging
from datetime import datetime, timedelta
from typing import Dict, List
import grpc
import os

from app import db
from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

from udaconnect_pb2 import (
    CreatePersonRequest,
    GetPersonRequest,
    GetAllPersonRequest,
    GetLocationRequest,
    FindContactsRequest,
)
from udaconnect_pb2_grpc import (
    PersonStub,
    LocationStub,
    ConnectionStub,
)

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

CORE_HOST = os.environ["CORE_HOST"]
CORE_PORT = os.environ["CORE_PORT"]

channel = grpc.insecure_channel(f"{CORE_HOST}:{CORE_PORT}")

person_stub = PersonStub(channel)
location_stub = LocationStub(channel)
connection_stub = ConnectionStub(channel)

def convert_location_message_to_model(message):
    location = Location(
        id=message.id,
        person_id=message.person_id,
        creation_time=datetime.fromtimestamp(message.creation_time),
    )
    location.set_wkt_with_coords(message.latitude, message.longitude)
    return location

def convert_person_message_to_model(message):
    return Person(
        id=message.id,
        first_name=message.first_name,
        last_name=message.last_name,
        company_name=message.company_name,
    )

class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: str, end_date: str, meters=5
    ) -> List[Connection]:
        """
        Finds all Person who have been within a given distance of a given Person within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """

        resp = connection_stub.FindContacts(FindContactsRequest(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            distance=meters
        ))

        return list(map(lambda contact: Connection(
            location=convert_location_message_to_model(contact.location),
            person=convert_person_message_to_model(contact.person),
        ), resp.contacts))

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        resp = location_stub.Get(GetLocationRequest(id=location_id))
        location = Location(
            id=resp.data.id,
            person_id=resp.data.person_id,
            creation_time=datetime.fromtimestamp(resp.data.creation_time),
        )
        location.set_wkt_with_coords(resp.data.latitude, resp.data.longitude)
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db.session.add(new_location)
        db.session.commit()

        return new_location


class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        resp = person_stub.Create(CreatePersonRequest(
            first_name=person["first_name"],
            last_name=person["last_name"],
            company_name=person["company_name"],
        ))
        return Person(
            id=resp.data.id,
            first_name=resp.data.first_name,
            last_name=resp.data.last_name,
            company_name=resp.data.company_name,
        )

    @staticmethod
    def retrieve(person_id: int) -> Person:
        resp = person_stub.Get(GetPersonRequest(id=person_id))
        return Person(
            id=resp.data.id,
            first_name=resp.data.first_name,
            last_name=resp.data.last_name,
            company_name=resp.data.company_name,
        )


    @staticmethod
    def retrieve_all() -> List[Person]:
        resp = person_stub.GetAll(GetAllPersonRequest())
        return list(
            map(lambda person: Person(
                id=person.id,
                first_name=person.first_name,
                last_name=person.last_name,
                company_name=person.company_name,
            ), resp.list)
        )
