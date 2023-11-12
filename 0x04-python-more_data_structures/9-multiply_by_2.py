#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''
    dictionary with all values multiplied by 2

    Args:
        a_dictionary: dict OF INTEGERS

    Returns:
        a new dict
    '''

    return {key: value*2 for key, value in a_dictionary.items()}
