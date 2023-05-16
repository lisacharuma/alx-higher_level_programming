#!/usr/bin/python3
"""uses 2 for loops to print matrix"""


def print_matrix_integer(matrix=[[]]):
    """outer loop for rows"""
    for i in matrix:
        """inner loop for columns"""
        for j in i:
            print("{:d}".format(j), end=" " if j != i[-1] else "")
        print()
