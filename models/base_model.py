"""
this module contains the base class for all table
"""
from datetime import datetime
from uuid import uuid4
from models.engine import storage, DB_TYPE
from sqlalchemy import String, TextAsFrom, MetaData, Column, DateTime
from sqlalchemy.orm import declarative_base

metadata = MetaData()
if DB_TYPE == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:

    if DB_TYPE == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False)
        updated_at = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):

        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid4())

        if len(kwargs) >= 1:
            for key in kwargs.keys():
                self.__dict__[key] = kwargs[key]

        storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    @staticmethod
    def save():
        storage.save()

    def to_dict(self):
        dicti = self.__dict__.copy()
        dicti["updated_at"] = self.updated_at.isoformat()
        dicti["created_at"] = self.created_at.isoformat()
        dicti["__class__"] = self.__class__.__name__

        return dicti
