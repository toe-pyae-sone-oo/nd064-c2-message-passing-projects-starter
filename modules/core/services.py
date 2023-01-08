from typing import Dict, List
from models import Person
from app import db


class PersonService:
    
    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person
