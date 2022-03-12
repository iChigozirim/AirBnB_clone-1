#!/usr/bin/python3
""" City Module for HBNB project """
import imp
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """Represents a table on the database MySQL.

    Attributes:
        __tablename__ (str): The table name.
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"),  nullable=False)
    place = relationship("place", backref="cities", cascade="all, delete")
