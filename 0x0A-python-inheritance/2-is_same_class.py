#!/usr/bin/python3
""" Checks if an object is an instance of a class """


def is_same_class(obj, a_class):
    """ check if instance obj belongs to a_class """
    return type(obj) == a_class
