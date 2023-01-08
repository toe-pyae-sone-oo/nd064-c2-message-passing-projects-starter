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
