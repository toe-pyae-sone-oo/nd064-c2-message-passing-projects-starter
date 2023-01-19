import logging
import sys

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

logger = setup_logger()