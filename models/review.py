#!/usr/bin/python3
<<<<<<< HEAD
""" Review module for the HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
=======
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table reviews.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place id.
        user_id (sqlalchemy String): The review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
>>>>>>> e6b3d3489ff16aa372d5bf7d1090bd04b06cf8bb
