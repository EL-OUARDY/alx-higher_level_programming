#!/usr/bin/python3
""" defines a BaseGeometryi class """


class BaseGeometry:
    """ this is BaseGeometry class representation """

    def area(self):
        """ for now, throw a custom error """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
