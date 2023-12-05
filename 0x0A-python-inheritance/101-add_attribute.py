#!/usr/bin/python3
""" Module defines add_attribute function """


def add_attribute(obj, att, value):
    """ adds a new attribute to an object if it’s possible """
    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
