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

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get the list of cities related to the state."""
            city_list = []
            all_city = models.storage.all(City)
            for city in all_city.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
