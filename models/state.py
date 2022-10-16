#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete, delete-orphan", backref="state")
    
    @property
    def cities(self):
        """ returns the list of City instances with state_id """
        import models
        from models.city import City
        cities = []
        for city in models.storage.all(City).values():
                if self.id == city.id:
                    cities.append(city)
        return cities
