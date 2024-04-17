#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv

storage_engine = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    if (storage_engine == "db"):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                            back_populates='state')
    else:
        name = ""

    @property
    def cities(self):
        """The cities property."""
        city_list = []
        for i in storage.all(City).values():
            if i.state_id == self.id:
                city_list.append(i)
        return city_list
