"""
This module contains the school account -->
"""
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os

DB_TYPE = os.getenv('DB_TYPE')


class StudentResult(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "results"
        student_id = Column(String(40), ForeignKey("registered_students.id"), nullable=False)
        test_id = Column(String(40), ForeignKey("uploaded_test.id"), nullable=False)
        score = Column(Integer, nullable=False)
        test = relationship("SchoolTest", backref='results')
        student = relationship("Student", backref='results')

    else:
        student_id = ""
        test_id = ""
        score = 0


class StudentSubmit(BaseModel, Base):
    __tablename__ = 'submitted_test_info'
    student_id = Column(String(40), ForeignKey("registered_students.id"), nullable=False)
    test_id = Column(String(40), ForeignKey("school_files.id"), nullable=False)
    score = Column(Integer)
    file_ext = Column(String(10), nullable=False)
    test = relationship("SchoolFiles", backref='results')
    student = relationship("Student", backref='result')

