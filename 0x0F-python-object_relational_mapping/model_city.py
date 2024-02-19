#!/usr/bin/python3
""" City module of course """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class will inherit from Base class

    Attributes:
        __tablename__ (str): name of the table.
        id (int): unique identifier for city (primary key).
        name (str): name of city.
        state_id (int): id of state (foreign key)

    Usage:
        Define class that represent city in database
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return f"{self.state_id}: ({self.id}) {self.name}"
