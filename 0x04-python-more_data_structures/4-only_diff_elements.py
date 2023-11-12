#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''
    returns a set of all elements present in only one set

    Args:
        set_1: input set
        set_2: input set

    Returns:
        a set
    '''

    return set_1 ^ set_2
