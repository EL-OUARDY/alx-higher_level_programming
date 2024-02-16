#!/usr/bin/python3
"""
This script prints all City objects
from the database hbtn_0e_14_usa
using SQLAlchemy ORM
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    # create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # prints all city records alongside their state
    cities = session.query(City, State).join(State).order_by(City.id)
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # close the session
    session.close()
