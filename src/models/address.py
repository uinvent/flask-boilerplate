"""
Address Model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class AddressModel(BaseModel):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, nullable=False)
    line_1 = Column(String(300), nullable=False)
    line_2 = Column(String(300), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    zip_code = Column(String(10), nullable=True)
    person_id = Column(ForeignKey('person.id'), nullable=False)
    person = relationship('PersonModel')
