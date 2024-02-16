#!/usr/bin/python3
"""
This module contains the class definition of a city
"""

from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    """City class representation"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    # state = relationship("State", back_populates="cities")
