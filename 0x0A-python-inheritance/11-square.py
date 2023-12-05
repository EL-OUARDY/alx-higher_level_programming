#!/usr/bin/python3
""" represent Square class - a Rectangle subclass """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class body """

    def __init__(self, size):
        """ constructor """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    # inherits str() from Rectangle base class
