#!/usr/bin/python3
"""
This module implement generating Pascal's triangle
"""


def pascal_triangle(n):
    """ This function generate Pascal's triangle of nth row
    which returns a list of lists of integers representing
    the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    Assumption: You can assume n will be always an integer
    """

    # Declare lists in list with initail value of 1
    triangle = [[1], [1, 1]]

    # If n is zero or negative return []
    if n <= 0:
        return [[]]

    # If n = 1 return [1]
    if n == 1:
        return [[1]]

    # If n = 2 return [[1], [1, 1]]
    if n == 2:
        return triangle

    # If n >= 3 then pascal's triangle dynamic computation
    # starts here
    if n >= 3:
        flag = 0
        for i in range(0, n - 2):
            j = 0
            # Create new list in every iteration
            new_row = []
            # Beginning of new row
            if flag == 0:
                new_row.append(1)
            while j <= i:
                new_row.append(triangle[-1][j] + triangle[-1][j + 1])
                j += 1
            flag = 1
            if flag == 1:
                # End of new row
                new_row.append(1)
                # return flag to 0
                flag = 0
            triangle.append(new_row)

    return triangle
