#!/usr/bin/python3
""" module contains a function that JSON serialize a class """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object """

    return vars(obj)
