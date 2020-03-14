"""
Person entity specific service
"""
from src.services.base import BaseService
from src.repositories.person import PersonRepository


class PersonService(BaseService):
    def __init__(self):
        BaseService.__init__(self, PersonRepository)
