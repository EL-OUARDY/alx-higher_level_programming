#!/usr/bin/python3
""" square class """


class Square:
    """ square class definition"""

    def __init__(self, size=0):
        """initialize square class
        Args:
            size: square object's size
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ calculate the square area

        Returns:
            integer, square area
        """

        return (self.__size ** 2)
