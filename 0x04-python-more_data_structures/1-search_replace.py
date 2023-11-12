#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    replaces all occurrences of an element by another in a new list

    Args:
        my_list: input list
        search: element to be replaced
        replace: the new element
    Returns:
        new list with replaced values
    '''

    new_list = list(map(lambda x: replace if x == search else x, my_list))

    return new_list
