#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            n[row][col] = matrix[row][col] * matrix[row][col]
    return n
