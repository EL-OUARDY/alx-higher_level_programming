#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):  # sub-class of unittest.TestCase
    """ Define unittests for max_integer([]) """

    def test_empty_list(self):
        """ empty list case """
        self.assertEqual(max_integer([]), None)

    def test_first_is_max(self):
        """ first is max """
        max_at_beginning = [99, 65, 11, 76]
        self.assertEqual(max_integer(max_at_beginning), 99)

    def test_ordered_list(self):
        """ ordered list of integers """
        ordered = [0, 1, 2, 3]
        self.assertEqual(max_integer(ordered), 3)

    def test_unordered_list(self):
        """ unordered list of integers """
        unordered = [2, 1, 7, 0]
        self.assertEqual(max_integer(unordered), 7)

    def test_string(self):
        """ string case """
        string = "elouardy"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """ list of strings """
        strings = ["papa", "mama", "yaya", "tata"]
        self.assertEqual(max_integer(strings), "yaya")

    def test_empty_string(self):
        """ empty string """
        self.assertEqual(max_integer(""), None)

    def test_space_string(self):
        """ space string """
        self.assertEqual(max_integer(" "), " ")

    def test_floats(self):
        """ floats case  """
        floats = [2.11, 3.14, 0.33, -1.5]
        self.assertEqual(max_integer(floats), 3.14)

    def test_list_with_one_item(self):
        """ list has one element """
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats_ints(self):
        """ mixed list of floats and ints """
        ints_and_floats = [7, 3.14, 15, -6, 7, 19.9, 8]
        self.assertEqual(max_integer(ints_and_floats), 19.9)


if __name__ == '__main__':  # if the script is executed independently
    unittest.main()  # run unit test
