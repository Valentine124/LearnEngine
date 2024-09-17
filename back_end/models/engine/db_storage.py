"""
This module contains the class and methods that
will be used to manage the database for the app
"""


import sqlalchemy
from models.resources import Resources, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """ Interact with MySQL database """

    __engine = None
    __session = None

    def __init__(self):
        """ Instanciate DBStorage object """

        MYSQL_USER = 'le_user'
        MYSQL_PWD ='le_pwd'
        MYSQL_HOST = 'localhost'
        MYSQL_DB = 'le_db'

        self.__engine = create_engine(f'mysql+mysqldb://{MYSQL_USER}:'\
                                      f'{MYSQL_PWD}@{MYSQL_HOST}/'\
                                      f'{MYSQL_DB}')

    def all_resources(self):
        """ Return all objects of resources """

        res_dict = {}
        res_list = self.__session.query(Resources).all()

        for res_obj in res_list:
            res_dict[res_obj.title] = res_obj.to_dict()

        return res_dict

    def new(self, obj):
        """ Add an item to the database """

        self.__session.add(obj)

    def save(self):
        """ Commit all changes """

        self.__session.commit()

    def reload(self):
        """ Create the engine """

        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session

    def close(self):
        """ Remove session """

        self.__session.remove()
