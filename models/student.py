"""
This module contains the student account table -->
"""
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os
from flask_login import UserMixin

DB_TYPE = os.getenv('DB_TYPE')


class Student(BaseModel, Base, UserMixin):
    if DB_TYPE == "db":
        __tablename__ = "registered_students"
        first_name = Column(String(40), nullable=False)
        last_name = Column(String(40), nullable=False)
        school_id = Column(String(40), ForeignKey('registered_schools.id', ondelete="CASCADE"), nullable=False)
        class_id = Column(String(40), ForeignKey('classes.id'))
        role = Column(String(15), nullable=False)
        gmail = Column(String(40), nullable=False, unique=True)
        password = Column(String(60), nullable=False, unique=True)
        status = Column(Boolean, default=False)
        school = relationship("School", backref="students")

    else:
        first_name = ""
        second_name = ""
        class_ = ""
        gmail_address = ""
        password = ""
        status = False


class Notification(BaseModel, Base):
    __tablename__ = 'notifications'
    school_id = Column(String(40), ForeignKey('registered_schools.id'), nullable=False)
    class_id = Column(String(40), ForeignKey('classes.id'), nullable=False)
    message = Column(String(700), nullable=False)
    class_ = relationship('Classes', backref='messages')
    school = relationship('School', backref='messages')
