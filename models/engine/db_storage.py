"""
This file contains the DBMS manipulating function
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.sch_acc import Classes, School, ProfilePic, SchoolStrictUsers
from models.student import Student, Notification
from models.school_test import SchoolTest, SchoolFiles
from models.student_result import StudentResult, StudentSubmit

classes = {
            "School": School,
            "SchoolTest": SchoolTest,
            "Student": Student,
            "StudentResult": StudentResult,
            "Classes": Classes,
            'SchoolFiles': SchoolFiles,
            'StudentSubmit': StudentSubmit,
            'Notification': Notification,
            'ProfilePic': ProfilePic,
            'SchoolStrictUsers': SchoolStrictUsers
        }


class Storage:
    __engine = None
    __session = None

    def __init__(self):

        DB_PASSWD = getenv("DB_PASSWD", None)
        DB_HOST = getenv("DB_HOST", None)
        DB_CHANNEL = "mysql+mysqldb"
        DB_USER = getenv("DB_USER", None)
        DB_NAME = getenv("DB_NAME", None)

        self.__engine = create_engine("{}://{}:{}@{}/{}".format(
            DB_CHANNEL,
            DB_USER,
            DB_PASSWD,
            DB_HOST,
            DB_NAME
        ))
        # self.__engine = create_engine('sqlite:///example12311.db', echo=True)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def session(self):
        return self.__session

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        # Base.metadata.bind = self.__engine
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
