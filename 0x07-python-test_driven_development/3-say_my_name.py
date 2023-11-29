#!/usr/bin/python3
"""" This module contains a function that prints a passed name """


def say_my_name(first_name, last_name=""):
    """ prints name (<first name> <last name>)

    Args:
        first_name (str): 1st arg
        last_name (str): 2nd arg

    Raises:
        TypeError: first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
