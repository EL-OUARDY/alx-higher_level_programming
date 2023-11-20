#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ Safely divides element by element 2 lists

    Args:
        my_list_1 (list): first list
        my_list_2 (list): second list
        list_length (int): number of elements to divide

    Returns:
        new list with all divisions
    """

    divisions = []

    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            divisions.append(div)
    return divisions
