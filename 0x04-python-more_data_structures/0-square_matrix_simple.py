#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    computes the square value of all integers of a matrix

    Args:
        matrix: 2D array

    Returns:
        a 2D array contains all squared values
    '''

    return [[x**2 for x in row] for row in matrix]
