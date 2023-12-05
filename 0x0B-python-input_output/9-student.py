#!/usr/bin/python3
""" this module contains strudent class """


class Student:
    """ student class representation """

    def __init__(self, first_name, last_name, age):
        """ initializes Student class objects """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return vars(self)
