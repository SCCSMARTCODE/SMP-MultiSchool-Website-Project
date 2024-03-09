"""
This module contains the student account table -->
"""
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os

DB_TYPE = os.getenv('DB_TYPE')


# class Student(BaseModel, Base):
#     if DB_TYPE == "db":
#         __tablename__ = "registered_student"
#         first_name = Column(String(40), nullable=False)
#         second_name = Column(String(40), nullable=False)
#         school_id = Column(String(40), ForeignKey('registered_schools.id', ondelete="all, delete"), nullable=False)
#         class_ = Column(String(20), nullable=False)
#         gmail_address = Column(String(40), nullable=False, unique=True)
#         password = Column(String(15), nullable=False, unique=True)
#         status = Column(Boolean, default=False)
#         test = relationship("StudentResult", backref='student')

class Student(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "registered_student"
        first_name = Column(String(40), nullable=False)
        second_name = Column(String(40), nullable=False)
        school_id = Column(String(40), ForeignKey('registered_schools.id', ondelete="CASCADE"), nullable=False)
        class_ = Column(String(20), nullable=False)
        gmail_address = Column(String(40), nullable=False, unique=True)
        password = Column(String(15), nullable=False, unique=True)
        status = Column(Boolean, default=False)
        school = relationship("School", backref="student")

    else:
        first_name = ""
        second_name = ""
        class_ = ""
        gmail_address = ""
        password = ""
        status = False
