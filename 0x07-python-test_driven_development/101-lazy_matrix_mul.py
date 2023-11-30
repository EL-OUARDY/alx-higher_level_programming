#!/usr/bin/python3

""" Module defines a function multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Return the multiplication of two matrices.

    Args:
        m_a (matrix of ints/floats): first matrix.
        m_b (matrix of ints/floats): second matrix.
    """

    return (np.matmul(m_a, m_b))  # NumPy magic
