#!/usr/bin/python3
def print_last_digit(number):
    '''
    print last digit of a number

    Arguments:
    number: target string

    Returns:
    number - last digit
    '''
    if number < 0:
        number = -number    # abs value

    last_digit = number % 10

    print("{:d}".format(last_digit), end="")

    return last_digit
