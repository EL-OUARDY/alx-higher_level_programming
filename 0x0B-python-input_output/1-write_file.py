#!/usr/bin/python3
""" this moducle contains only read_file function """

def write_file(filename="", text=""):
    """ write text in a given file """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)  #  the number of characters written
