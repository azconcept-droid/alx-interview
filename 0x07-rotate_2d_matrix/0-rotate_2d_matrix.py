#!/usr/bin/python3
""" Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """ This function rotate 2D matrix in-place"""

    # matrix dimension
    n = len(matrix)

    # Initialize temporary matrix of n x n with zeros
    tmp = [[0] * n for _ in range(n)]

    # Flip the matrix clockwise
    for i in range(n):
        for j in range(n):
            tmp[j][n - i - 1] = matrix[i][j]

    # update the matrix in-place
    for i in range(n):
        for j in range(n):
            matrix[i][j] = tmp[i][j]
