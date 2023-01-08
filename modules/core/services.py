import os
import logging
from typing import Dict, List
from kafka import KafkaProducer
from models import Person
from app import db


KAFKA_SERVER = os.environ["KAFKA_SERVER"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-core")

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class PersonService:
    
    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)

        producer.send(TOPIC_NAME, b"hello!")
        producer.flush()

        logger.info("message sent!")

        return person
    
    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()

    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return new_person