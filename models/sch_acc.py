"""
This module contains the school account -->
"""
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.engine import DB_TYPE


class School(BaseModel, Base):

    if DB_TYPE == "db":
        __tablename__ = "registered_schools"
        name = Column(String(40), unique=True, nullable=False)
        address = Column(String(300), unique=True, nullable=False)
        gmail = Column(String(40), unique=True, nullable=False)
        phone_address = Column(String(30), unique=True, nullable=False)
        password = Column(String(20), unique=True, nullable=False)
        status = Column(Boolean, default=False)
        student = relationship('Student', cascade='all, delete', backref="school")
        text = relationship('SchoolTest', cascade='all, delete', backref="school")
    else:
        name = ""
        address = ""
        gmail = ""
        phone_address = ""
        password = ""
        status = False


class Student(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "registered_student"
        first_name = Column(String(40), nullable=False)
        second_name = Column(String(40), nullable=False)
        school_id = Column(String(40), ForeignKey('registered_schools.id', ondelete="all, delete"), nullable=False)
        class_ = Column(String(20), nullable=False)
        gmail_address = Column(String(40), nullable=False, unique=True)
        password = Column(String(15), nullable=False, unique=True)
        status = Column(Boolean, default=False)
        test = relationship("SchoolTest", backref='student')

    else:
        first_name = ""
        second_name = ""
        class_ = ""
        gmail_address = ""
        password = ""
        status = False


class SchoolTest(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "uploaded_test"
        school_id = Column(String(40), ForeignKey("registered_schools.id"), nullable=False)
        topic = Column(String(50), nullable=False)
        subject = Column(String(40), nullable=False)
        class_ = Column(String(20), nullable=False)
        instruction = Column(String(60))
        content = Column(String(10000000), nullable=False)
        no_of_questions = Column(Integer, nullable=False)
        relationship("StudentResult", backref='test')
    else:
        school_id = ""
        topic = ""
        subject = ""
        class_ = ""
        instruction = ""
        content = ""
        no_of_questions = 0


class StudentResult(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "results"
        student_id = Column(String(40), ForeignKey("registered_student.id"), nullable=False)
        test_id = Column(String(40), ForeignKey("SchoolTest"), nullable=False)
        score = Column(Integer, nullable=False)
    else:
        student_id = ""
        test_id = ""
        score = 0
