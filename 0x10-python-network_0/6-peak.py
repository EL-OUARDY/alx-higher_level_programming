#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Finds the peak

    Arguments:
        list_of_integers: list of unsorted integers
    Returns:
        peak integer
    """
    left, right = 0, len(list_of_integers) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if mid < len(list_of_integers) - 1 and (
            list_of_integers[mid] < list_of_integers[mid + 1]
            or (
                mid - 1 > 0
                and list_of_integers[mid] == list_of_integers[mid - 1]
            )
        ):
            left = mid + 1
        elif mid > 0 and (
            list_of_integers[mid] < list_of_integers[mid - 1]
            or (
                mid + 1 < len(list_of_integers) - 1
                and list_of_integers[mid] == list_of_integers[mid + 1]
            )
        ):
            right = mid - 1
        else:
            return list_of_integers[mid]
