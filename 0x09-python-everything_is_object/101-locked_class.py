#!/usr/bin/python3
""" defines a locked class """


class LockedClass:
    """ allows only instances with first_name attribute """

    __slots__ = ["first_name"]
