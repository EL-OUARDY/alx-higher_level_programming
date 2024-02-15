#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
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
    state_name = argv[4]

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

    # get state record with the target name passed as argument
    state = session.query(State).filter(State.name == state_name).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # close the session
    session.close()
