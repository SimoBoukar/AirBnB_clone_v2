#!/usr/bin/python3
"""
    DBStorage class for SQLAlchemy
"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from os import environ, getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

tables = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """SQLAlchemy database interaction commands"""
    __engine = None
    __session = None

    def __init__(self):
        """Init a DBStorage object"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.
                format(user, password, host, database), pool_pre_ping=True
                )

        if (env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current session and list all instances of class"""
        dictionary = {}
        if cls:
            for ins in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, ins.id)
                dictionary[key] = ins
        else:
            for table in tables:
                cls = tables[table]
                for ins in self.__session.query(cls).all():
                    key = "{}.{}".format(cls.__name__, ins.id)
                    dictionary[key] = ins
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload method"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(Session)
        self.__session = Scope
