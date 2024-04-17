#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if (models.storage_engine == "db"):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                            back_populates='state')
    else:
        name = ""

    if models.storage_engine != "db":
        @property
        def cities(self):
            """Get the list of cities related to the state."""
            city_list = []
            for i in storage.all(City).values():
                if i.state_id == self.id:
                    city_list.append(i)
            return city_list
