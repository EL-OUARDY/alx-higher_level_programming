#!/usr/bin/python3

""" This module defines matrix division function """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix

    Args:
        matrix: list of lists 2D list, values are (ints) or (floats)
        div: integer/float for matrix division
    Raises:
        TypeError: matrix is a list of lists of integers or floats
        TypeError: matrix's rows are different in size
        TypeError: div is not integer/float
        ZeroDivisionError: div equal 0
    Returns:
        new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or  # not list or empty
            not all(isinstance(row, list) for row in matrix) or  # wrong matrix
            not all(isinstance(cell, (int, float))  # cells are integers/floats
                    for cell in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

        # all lists have same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):  # div is integer/float
        raise TypeError("div must be a number")

    if div == 0:  # div equal zero
        raise ZeroDivisionError("division by zero")

        # apply division
    new_node = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return new_node
