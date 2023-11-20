#!/usr/bin/python3

def safe_function(fct, *args):
    """ Safely call a function

    Args:
        fct (function pointer): function to be called
        args (list): function arguments

    Returns:
        fct's result, OR None if something goes wrong
    """
    try:
        return fct(*args)
    except Exception as ex:
        import sys
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
