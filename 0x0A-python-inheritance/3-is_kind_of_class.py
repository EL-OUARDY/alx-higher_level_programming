#!/usr/bin/python3
""" check if object is an instance of a class or an inherited class """


def is_kind_of_class(obj, a_class):
    """ check if obj is instance of a_class or one its derived classes """
    return (isinstance(obj, a_class))
