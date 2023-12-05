#!/usr/bin/python3
""" this module defines a custom class MyInt that inherits from builtin int """


class MyInt(int):
    """ invert int operators == and != """

    def __eq__(self, value):
        """ redefine == opeartor with != """
        return self.real != value

    def __ne__(self, value):
        """ redefine != operator with == """
        return self.real == value
