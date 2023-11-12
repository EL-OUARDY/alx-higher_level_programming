#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    adds all unique integers in a list (only once for each integer)

    Args:
        my_list: input list

    Returns:
        integer - sum of unique elements
    '''

    unique_list = list(set(my_list))

    sum = 0
    for x in unique_list:
        sum += x

    return sum
