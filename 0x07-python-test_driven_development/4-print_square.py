#!/usr/bin/python3
"""

This module contain a function that prints a square with hashes

"""


def print_square(size):
    """ prints a square with the character #

    Args:
        size (int): the size of the square

    Raises:
        TypeError: size is not an integer
        TypeError: size is a float and less than zero
        ValueError: size is negative
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # draw the square
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")  # new line
