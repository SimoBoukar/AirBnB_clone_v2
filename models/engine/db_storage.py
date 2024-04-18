#!/usr/bin/python3
"""
    DBStorage class for SQLAlchemy
"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


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
                format(user, password, host, database), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current session and list all instances of class"""
        dictionary = {}
        if cls:
            if type(cld) is str:
                cls = eval(cls)
            q = self.__session.query(cls)
            for ins in q:
                key = "{}.{}".format(type(ins).__name__, ins.id)
                dictionary[key] = ins
        else:
            tables = [State, City, User, Place, Review, Amenity]
            for table in tables:
                q = self.__session.query(table)
                for ins in q:
                    key = "{}.{}".format(type(ins).__name__, ins.id)
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
        self.__session = Scope()
