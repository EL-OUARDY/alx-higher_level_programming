#!/usr/bin/python3

""" This module defines matrix_mul function """


def matrix_mul(m_a, m_b):
    """multiplies 2 matrice

    Args:
        m_a: 1st input matrix
        m_b: 2nd input matrix
    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a matrix
        ValueError: if m_a or m_b is empty
        TypeError: if m_a or m_b contains non int/float
        TypeError: if m_a or m_b is not rectangular
        TypeError: can't be multiplied
    Returns:
        result matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or not all(row != [] for row in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or not all(row != [] for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(
        isinstance(num, (int, float))  # m_a cells are integers/floats
        for num in [cell for row in m_a for cell in row]
    ):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
        isinstance(num, (int, float))  # m_b cells are integers/floats
        for num in [cell for row in m_b for cell in row]
    ):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):  # compare m_a columns & m_b rows
        raise ValueError("m_a and m_b can't be multiplied")

    cols = len(m_b[0])  # m_b columns
    rows = len(m_a)  # m_a rows
    result_list = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(len(m_b)):
                result_list[i][j] += m_a[i][k] * m_b[k][j]

    return result_list
