#!/usr/bin/python3
""" this module contains a JSON deserialization function """
import json


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string """
    return json.loads(my_str)
