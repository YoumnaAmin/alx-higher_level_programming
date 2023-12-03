#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            space = ""
            for col in i:
                print("{:s}{:d}".format(space, col), end="")
                space = " "
            print()
