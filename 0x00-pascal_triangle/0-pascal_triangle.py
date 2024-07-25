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

    # If n >= 3 then pascal's triangle computation starts here
    if n >= 3:
        # for i in range(0, n): # Print nth row of 0th indexing
        new_row = []
        # if i = 0 element is 1
        new_row.append(1) # 1st edge
        new_row.append(triangle[1][0] + triangle[1][1])
        # if i = n - 1 element is 1
        new_row.append(1) # 2nd edge
        triangle.append(new_row)
        # for n = 3 stop here

        new_row = []
        # if i = 0 element is 1
        new_row.append(1) # 1st edge
        new_row.append(triangle[2][0] + triangle[2][1])
        new_row.append(triangle[2][1] + triangle[2][2])
        # if i = n - 1 element is 1
        new_row.append(1) # 2nd edge
        triangle.append(new_row)
        # for n = 4 stop here

        new_row = []
        # if i = 0 element is 1
        new_row.append(1) # 1st edge
        new_row.append(triangle[3][0] + triangle[3][1])
        new_row.append(triangle[3][1] + triangle[3][2])
        new_row.append(triangle[3][2] + triangle[3][3])
        # if i = n - 1 element is 1
        new_row.append(1) # 2nd edge
        triangle.append(new_row)
        # for n = 5 stop here
            
    return triangle
