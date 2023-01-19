from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import sys


db = SQLAlchemy()

def create_app(env=None):
    from config import config_by_name

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])

    db.init_app(app)
    
    return app

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

app = create_app()

logger = setup_logger()