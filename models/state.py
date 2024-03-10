#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        cites = []

    def cities(self):
        """Returns the list of City objects linked to the current State"""
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        cities = []
        for key, value in storage.all().items():
            if isinstance(value, City) and value.state_id == self.id:
                cities.append(value)
        return cities
    