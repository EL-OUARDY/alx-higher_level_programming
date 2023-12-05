#!/usr/bin/python3
""" module contains load_from_json_file function """
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, mode="r", encoding="utf-8") as file:
        json_obj_string = file.read()
        return json.loads(json_obj_string)
