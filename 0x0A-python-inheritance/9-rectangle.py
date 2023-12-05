#!/usr/bin/python3
""" a class inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ define rectangle by using BaseGeometry """

    def __init__(self, width, height):
        """ construstor """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ return rectangle description: [Rectangle] <width>/<height> """
        string = (f"[{str(self.__class__.__name__)}] "
                  f"{str(self.__width)}/{str(self.__height)}")
        return string
