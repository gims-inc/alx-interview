#!/usr/bin/python3
"""
Returns a nested list of pascals triangle with values
"""


def pascal_triangle(n):
    """
    A simple function that return a list ao values in
    the pascal triangle for a given height

    n : int
        the height of the triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for height in range(n):
            row = []
            for col in range(height + 1):
                if col == 0 or col == height:
                    row.append(1)
                else:
                    row.append(triangle[height - 1][col - 1] +
                               triangle[height - 1][col])
            triangle.append(row)
        return triangle
