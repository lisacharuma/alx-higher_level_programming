#!/usr/bin/python3
"""Pascal's triangle module"""


def pascal_triangle(n):
    """A function that prints the pascal's triangle
    Arg: n is number of rows
    """
    p_triangle = []
    for row in range(n):
        this_row = []
        for column in range(row + 1):
            if column == 0 or column == row:
                this_row.append(1)
            else:
                prev_row = p_triangle[row - 1]
                this_row.append(prev_row[column] + prev_row[column - 1])
        p_triangle.append(this_row)
    return (p_triangle)
