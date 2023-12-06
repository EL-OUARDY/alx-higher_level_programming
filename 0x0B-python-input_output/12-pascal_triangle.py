#!/usr/bin/python3
""" module contains pascal_triangle function """


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n """
    triangle = []

    if n <= 0:  # invalid size
        return triangle

    for i in range(n):
        row = [1] * (i + 1)  # initialize all cells with 1
        for j in range(i + 1):
            if i == 0:  # skip first row
                continue

            prev = 0 if j == 0 else triangle[i - 1][j - 1]
            next = 0 if j == i else triangle[i - 1][j]
            row[j] = prev + next
        triangle.append(row)
    return triangle
