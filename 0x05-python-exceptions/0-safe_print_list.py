#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Safely print x elememts of a list

    Args:
        my_list (list): target list
        x (int): number of elements to print

    Returns:
        the number of elements printed
    """
    printed = 0

    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            printed += 1
        except IndexError:  # raised means index out of range
            break
    print("")  # new line
    return printed
