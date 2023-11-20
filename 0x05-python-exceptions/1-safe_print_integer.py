#!/usr/bin/python3

def safe_print_integer(value):
    """ Safely print an integer

    Args:
        value (any type): expected integer to be printed

    Returns:
        boolean, true if printed, false if not
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
