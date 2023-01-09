import os
import sys
import logging
from kafka import KafkaConsumer
import json
import grpc

from udaconnect_pb2 import (
    CreateLocationRequest,
    LocationMessage,
)
from udaconnect_pb2_grpc import (
    LocationStub,
)

def setup_logger():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("udaconnect-kafka-consumer")

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    logger.addHandler(stderr_handler)

    logger.propagate = False

    kafka_logger = logging.getLogger('kafka')
    kafka_logger.setLevel(logging.WARN)

    return logger

TOPIC_NAME = os.environ["KAFKA_TOPIC"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
CONSUMER_GROUP = os.environ["KAFKA_CONSUMER_GROUP"]

logger = setup_logger()

def convert_json(json_bytes: bytes):
    myjson = json_bytes.decode('utf-8').replace("'", '"')
    return json.loads(myjson)

CORE_HOST = os.environ["CORE_HOST"]
CORE_PORT = os.environ["CORE_PORT"]

channel = grpc.insecure_channel(f"{CORE_HOST}:{CORE_PORT}")
location_stub = LocationStub(channel)

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER, group_id=CONSUMER_GROUP)
for message in consumer:
    location_data = convert_json(bytes(message.value))
    logger.debug(f"location_data: {location_data}")
    location_stub.Create(CreateLocationRequest(
        payload=LocationMessage(
            person_id=location_data["person_id"],
            longitude=location_data["longitude"],
            latitude=location_data["latitude"],
            creation_time=location_data["creation_time"],
        )
    ))