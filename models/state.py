#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          back_populates='state')

    @property
    def cities(self):
        """The cities property."""
        city_list = []
        for i in storage.all(City).values():
            if i.state_id == self.id:
                city_list.append(i)
        return city_list
