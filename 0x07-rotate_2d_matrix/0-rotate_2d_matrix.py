#!/usr/bin/python3
"""
Rotate 2D Matrix <in-place> Solution
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix,
    rotate it 90 degrees clockwise.
    """
    if not matrix or len(matrix) == 0:
        return

    n = len(matrix)

    # Step one transpose the matrix :swap the rows and columns so that
    # the rows become columns and the columns become rows
    #  =>transposed_matrix = [list(row) for row in zip(*matrix)]
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j -
                                    1] = matrix[i][n - j - 1], matrix[i][j]
