#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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

    # create California state
    state = State(name="California")
    # add San Francisco city to the California state
    state.cities.append(City(name="San Francisco"))

    session.add(state)

    # commit pending changes
    session.commit()

    # close the session
    session.close()
