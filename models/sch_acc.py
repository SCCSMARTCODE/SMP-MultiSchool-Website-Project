"""
This module contains the school account -->
"""
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os
from flask_login import UserMixin

DB_TYPE = os.getenv('DB_TYPE')


class School(BaseModel, Base, UserMixin):

    if DB_TYPE == "db":
        __tablename__ = "registered_schools"
        name = Column(String(40), unique=True, nullable=False)
        address = Column(String(300), nullable=False)
        gmail = Column(String(40), unique=True, nullable=False)
        phone_address = Column(String(30), unique=True, nullable=False)
        role = Column(String(15), nullable=False)
        password = Column(String(60), unique=True, nullable=False)
        status = Column(Boolean, default=False)
        strict_registration = Column(Boolean, default=False)
    else:
        name = ""
        address = ""
        gmail = ""
        phone_address = ""
        password = ""
        status = False


class Classes(BaseModel, Base):

    if DB_TYPE == "db":
        __tablename__ = "classes"
        name = Column(String(50), nullable=False)
        school_id = Column(String(60), ForeignKey('registered_schools.id'), nullable=False,)
        school = relationship('School', backref='classes')
        student = relationship('Student', backref='class_')

    else:
        name = ""
        school_id = ""


class ProfilePic(BaseModel, Base):
    __tablename__ = 'profile_pics'
    user_id = Column(String(60), unique=True, nullable=False)
    file_ext = Column(String(10), nullable=False)


class SchoolStrictUsers(BaseModel, Base):
    __tablename__ = 'strict_users'
    gmail = Column(String(60), nullable=False)
    school_id = Column(String(60), ForeignKey('registered_schools.id'), nullable=False,)
    school = relationship('School', backref='strict_users')
