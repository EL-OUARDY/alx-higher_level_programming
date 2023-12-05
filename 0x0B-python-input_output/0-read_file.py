#!/usr/bin/python3
""" this moducle contains only read_file function """


def read_file(filename=""):
    """ print the entire content of a given file """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
