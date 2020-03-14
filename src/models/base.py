"""
Handles shared methods between models
"""
from sqlalchemy import inspect
from src.models import db


class BaseModel(db.Model):
    __abstract__ = True

    @property
    def serialize(self):
        """
        Serialize object in DICT
        :return:
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}