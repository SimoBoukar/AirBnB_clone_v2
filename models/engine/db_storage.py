#!/usr/bin/python3
"""
    DBStorage class for SQLAlchemy
"""
from models.base_model import BaseModel, Base
from models import city, state, storage
from os import environ, getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



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

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, database), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    
