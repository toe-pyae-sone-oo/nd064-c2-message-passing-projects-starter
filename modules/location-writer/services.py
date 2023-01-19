import os
from typing import Dict
from kafka import KafkaProducer
from app import logger
import json

KAFKA_SERVER = os.environ["KAFKA_SERVER"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class LocationService:

    @staticmethod
    def create(location: Dict):
        producer.send(TOPIC_NAME, bytes(json.dumps(location), 'utf-8'))
        logger.debug("create location message sent!")
