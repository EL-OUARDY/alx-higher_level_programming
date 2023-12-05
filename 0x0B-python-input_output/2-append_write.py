#!/usr/bin/python3
""" this moducle contains only append_write function """


def append_write(filename="", text=""):
    """ append text in a given file """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)  # the number of characters written
