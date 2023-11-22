#!/usr/bin/python3
"""square class"""


class Square:
    """square class representation"""

    def __init__(self, size=0):
        """initialize square object
        Args:
            size: square object's size
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """getter: size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """set the square size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """calculate the area of the square

        Returns:
            integer, square area
        """

        return (self.__size ** 2)
