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
        student_id = Column(String(40), ForeignKey("registered_student.id"), nullable=False)
        test_id = Column(String(40), ForeignKey("uploaded_test.id"), nullable=False)
        score = Column(Integer, nullable=False)
        test = relationship("SchoolTest", backref='result')
        student = relationship("Student", backref='result')

    else:
        student_id = ""
        test_id = ""
        score = 0
