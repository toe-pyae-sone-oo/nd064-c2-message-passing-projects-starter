import os
import sys
import logging
from kafka import KafkaConsumer

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

    return logger

TOPIC_NAME = os.environ["KAFKA_TOPIC"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

logger = setup_logger()

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    logger.debug(message)