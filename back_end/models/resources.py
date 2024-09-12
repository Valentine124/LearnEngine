""" This module contains the blueprint for
the resources object """


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Resources(Base):
    """ Resource object blueprint and table
    for the database """

    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True)
    title = Column(String(126), nullable=False)
    description = Column(String(126), nullable=False)
    origin = Column(String(45), nullable=False)
    type = Column(String(45), nullable=False)
    url = Column(String(126), nullable=False)
