#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ Safely prints the first x elements of a list and only integers

    Args:
        my_list (list): list holds targeted elements
        x (int): expected integer to be printed

    Returns:
        integer, number of elements printed
    """

    printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            pass
    print("")  # new line
    return printed
