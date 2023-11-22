#!/usr/bin/python3
""" defines class square """


class Square:
    """square class implementation"""

    def __init__(self, size=0):
        """initialize square class object
        Args:
            size: square object's size
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
