#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
using SQLAlchemy ORM
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # get user input arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    # create an engine to connect to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database_name
        ),
        pool_pre_ping=True,
    )

    # create database tables based on models
    Base.metadata.create_all(engine)

    # create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # lists all City objects
    # <city id>: <city name> -> <state name>
    cities = session.query(City).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # close the session
    session.close()
