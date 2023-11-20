#!/usr/bin/python3

def safe_print_integer_err(value):
    """ Safe integer print with error message

    Args:
        value (any type): expected integer to be printed

    Returns:
        boolean, true if printed, false if not
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
