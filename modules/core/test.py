from typing import Dict
import json
from datetime import datetime


def async_create(location: Dict):
    return bytes(json.dumps(location), 'utf-8')


b = async_create({
    "name": "Toe",
    "age": 10,
    "creation_time": int(datetime.now().timestamp())
})

print(bytes(b).decode('utf-8'))