#!/usr/bin/python3
""" this module contains strudent class """


class Student:
    """ student class representation """

    def __init__(self, first_name, last_name, age):
        """ initializes Student class objects """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes must be retrieved """

        if (type(attrs) == list):  # attrs is valid list
            if (all(type(x) == str for x in attrs)):  # all items are strings
                return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return vars(self)  # return all attributes

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
