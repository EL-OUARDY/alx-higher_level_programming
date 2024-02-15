#!/usr/bin/python3
"""
This script adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    # add a new state with the name "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)

    # commit pending changes
    session.commit()

    # display new state id
    print(new_state.id)

    # close the session
    session.close()
