"""
Person Entity
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel


class PersonModel(BaseModel):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(DateTime(100))
    gender = Column(String(25))
    national_identifier= Column(String(100))
    addresses = relationship('AddressModel')

    def from_dict(self, req_dict):
        if req_dict.get('first_name') is None:
            raise Exception('Person first name cant be empty.')

        self.first_name = req_dict.get('first_name')
        self.middle_name = req_dict.get('middle_name')
        self.last_name = req_dict.get('last_name')

        self.date_of_birth = req_dict.get('date_of_birth')
        self.gender = req_dict.get('gender')
        self.national_identifier = req_dict.get('national_identifier')