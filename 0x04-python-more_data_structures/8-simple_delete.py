#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
    deletes a key in a dictionary.

    Args:
        a_dictionary: targeted dictionary
        key: key to delete

    Returns:
        a dict
    '''

    if a_dictionary.get(key):
        del a_dictionary[key]

    return a_dictionary
