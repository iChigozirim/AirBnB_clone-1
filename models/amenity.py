#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship(
            "Place", secondary="place_amenity", viewonly=False
        )
