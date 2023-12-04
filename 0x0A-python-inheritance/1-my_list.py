#!/usr/bin/python3
""" This module contains a class inherits from the list class """


class MyList(list):
    """ this class inherits from list class """
    def print_sorted(self):
        """ print a sorted list """
        print(sorted(self))
