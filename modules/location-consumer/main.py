import os
import json
from kafka import KafkaConsumer
from app import (app, logger)
from services import LocationService

TOPIC_NAME = os.environ["KAFKA_TOPIC"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
CONSUMER_GROUP = os.environ["KAFKA_CONSUMER_GROUP"]

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER,
    group_id=CONSUMER_GROUP,
)

for message in consumer:
    try:
        location = json.loads(message.value.decode("utf-8"))
        with app.app_context():
            new_location = LocationService.create(location)
            logger.debug(f"new location created. location={new_location}")
    except Exception as e:
        logger.error(f"error occurred: {e}")