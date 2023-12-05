#!/usr/bin/python3
""" this module contains JSON stringify function """


import json
def to_json_string(my_obj):
    """ returns the JSON representation of an object as a string """
    return json.dumps(my_obj)
