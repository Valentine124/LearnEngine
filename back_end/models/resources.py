""" This module contains the blueprint for
the resources object """


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Resources(Base):
    """ Resource object blueprint and table
    for the database """

    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(126), primary_key=True, nullable=False)
    description = Column(String(1026), nullable=True)
    origin = Column(String(45), nullable=False)
    type = Column(String(45), nullable=False)
    url = Column(String(126), nullable=False)
    img = Column(String(126), nullable=True)

    def to_dict(self):
        """ Return The dictionary representation of object """

        new_dict = self.__dict__.copy()

        if '_sa_instance_state' in new_dict.keys():
            del new_dict['_sa_instance_state']

        return new_dict
