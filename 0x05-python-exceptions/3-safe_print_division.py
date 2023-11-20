#!/usr/bin/python3

def safe_print_division(a, b):
    """ Safely divides 2 integers and prints the result

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        result of division, otherwise None
    """

    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        return result
    finally:
        print("Inside result: {}".format(result))
    return result
