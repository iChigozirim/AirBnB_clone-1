#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
