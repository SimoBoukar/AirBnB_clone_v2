#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade="delete",
            backref='state')

    @property
    def cities(self):
        variables = models.storage.all()
        list_city = []
        result_city = []
        for key in variables:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_city.append(variables[key])
        for elemnts in list_city:
            if (elemnts.state_id == self.id):
                result_city.append(elemnts)
        return (result_city)
