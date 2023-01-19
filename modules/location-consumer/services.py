from typing import Dict
from models import (
    Location,
)
from app import db
from geoalchemy2.functions import ST_Point
from datetime import datetime


class LocationService:

    @staticmethod
    def create(location: Dict) -> Location:
        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = datetime.fromtimestamp(location["creation_time"])
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db.session.add(new_location)
        db.session.commit()

        return new_location