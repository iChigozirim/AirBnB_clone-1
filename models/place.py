#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Float
from sqlalchemy import Table
from sqlalchemy import String
from sqlalchemy import Integer
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


association_table = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:

        @property
        def reviews(self):
            """Get a list of all reviews of a place."""
            return [
                review
                for review in models.storage.all(Review)
                if review.place_id == self.id
            ]

        @property
        def amenities(self):
            """Get/set a list of all amenities of a place."""
            amenity_list = []
            for amenity in models.storage.all():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity_obj):
            """Appends an Amenity id to amenities_id attribute."""
            if type(amenity_obj) == Amenity:
                self.amenity_ids.append(amenity_obj.id)
