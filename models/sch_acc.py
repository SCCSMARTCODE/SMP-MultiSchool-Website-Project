"""
This module contains the school account -->
"""
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os

DB_TYPE = os.getenv('DB_TYPE')


class School(BaseModel, Base):

    if DB_TYPE == "db":
        __tablename__ = "registered_schools"
        name = Column(String(40), unique=True, nullable=False)
        address = Column(String(300), unique=True, nullable=False)
        gmail = Column(String(40), unique=True, nullable=False)
        phone_address = Column(String(30), unique=True, nullable=False)
        password = Column(String(20), unique=True, nullable=False)
        status = Column(Boolean, default=False)
        # student = relationship('Student', cascade='all, delete-orphan', back_populates="school")
        # text =
    else:
        name = ""
        address = ""
        gmail = ""
        phone_address = ""
        password = ""
        status = False








