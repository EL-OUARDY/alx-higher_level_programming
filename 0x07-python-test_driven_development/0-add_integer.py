#!/usr/bin/python3

""" this module has contains add_integer function """


def add_integer(a, b=98):
    """ sum of a and b as integers

    Args:
        a: first argument
        b: second argument

    Returns:
        integer - the sum

    Raises:
        TypeError: If a or b are not integers or a floats
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
