#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
using SQLAlchemy ORM
"""

from sys import argv
from model_state import Base, State
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

    # delete all state records that contain the letter "a"
    states = session.query(State).filter(State.name.contains("a"))
    for state in states:
        session.delete(state)

    # commit pending changes
    session.commit()

    # close the session
    session.close()
