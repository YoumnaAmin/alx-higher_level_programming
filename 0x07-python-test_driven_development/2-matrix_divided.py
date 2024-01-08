#!/usr/bin/python3
"""Function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides elements of a matrix"""
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if not isinstance(matrix[r][c], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                                of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            matrix_cp = round(matrix[r][c] / div, 2)
    return matrix_cp
