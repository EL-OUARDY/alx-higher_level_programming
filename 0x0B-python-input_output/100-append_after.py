#!/usr/bin/python3
""" this module contains append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file,
    after each line containing a specific string """
    exists = False
    content = ""

    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            content += line
            # check if line contains the search_string
            if search_string in line:
                content += new_string
                exists = True

    if exists:  # search_string exists and added to the content
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(content)
