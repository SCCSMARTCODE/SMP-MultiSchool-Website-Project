"""
This module contains the school account -->
"""
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os

DB_TYPE = os.getenv('DB_TYPE')


class SchoolTest(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "uploaded_test"
        school_id = Column(String(40), ForeignKey("registered_schools.id"), nullable=False)
        topic = Column(String(50), nullable=False)
        subject = Column(String(40), nullable=False)
        class_ = Column(String(20), nullable=False)
        instruction = Column(String(60))
        content = Column(BLOB, nullable=False)
        no_of_questions = Column(Integer, nullable=False)
        school = relationship('School', cascade='all, delete', backref="tests")

    else:
        school_id = ""
        topic = ""
        subject = ""
        class_ = ""
        instruction = ""
        content = ""
        no_of_questions = 0


class SchoolFiles(BaseModel, Base):
    if DB_TYPE == "db":
        __tablename__ = "school_files"
        school_id = Column(String(40), ForeignKey("registered_schools.id"), nullable=False)
        description = Column(String(500), nullable=False)
        class_id = Column(String(50), ForeignKey('classes.id'), nullable=False)
        file_ext = Column(String(10), nullable=False)
        file_category = Column(String(20), nullable=False)
        school = relationship('School', backref="files")
        class_ = relationship('Classes', backref='files')

    else:
        school_id = ""
        description = ""
        class_ = ""
