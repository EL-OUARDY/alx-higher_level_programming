#!/usr/bin/python3
"""
This module contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """State class representation"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
