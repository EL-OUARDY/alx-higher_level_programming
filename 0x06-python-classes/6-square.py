#!/usr/bin/python3
"""square class"""


class Square:
    """square class definition"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize square object

        Args:
            size (int): square object's size
            position (int, int): position of the square - coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """square size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """square size setter"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """square position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the square position - setter
        Args:
            value (int, int): two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """calculate the area of the Square

        Returns:
            integer, square area
        """
        return self.__size * self.__size

    def position_print(self):
        """Returns the position in spaces."""
        position = ""
        if self.size == 0:
            return "\n"

        for _ in range(self.position[1]):
            position += "\n"

        for row in range(self.size):
            for _ in range(self.position[0]):
                position += " "
            for col in range(self.size):
                position += "#"
            position += "\n"

        return position


    def my_print(self):
        """Print the square with the # character."""
        print(self.position_print(), end='')
