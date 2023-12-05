#!/usr/bin/python3
""" script adds all arguments to a Python list and save them to a file """
import sys


if __name__ == "__main__":  # not imported!
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load("add_item.json")
    except FileNotFoundError:
        items = []

    arguments = sys.argv[1:]
    items.extend(arguments)  # append argumets to our list
    save(items, "add_item.json")
