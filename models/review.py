#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)