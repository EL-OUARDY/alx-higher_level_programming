#!/usr/bin/python3
"""square class"""


class Square:
    """square class representation"""

    def __init__(self, size=0):
        """initialize the square object
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
        """getter - get square size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter - set size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ calculate square area
        Returns:
            integer, square area
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()

        line = "#" * self.__size

        for i in range(self.__size):
            print(line)
