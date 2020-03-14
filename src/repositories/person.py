"""
Person entity specific repository
"""
from src.models.person import PersonModel
from src.repositories.base import BaseRepository


class PersonRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, PersonModel)
