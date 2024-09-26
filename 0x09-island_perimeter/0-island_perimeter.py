#!/usr/bin/python3
"""
This module calculate island perimeter
"""


def island_perimeter(grid):
    """Calculate the perimeter of an Island"""

    # Breadth of grid
    breadth = len(grid[0])

    # length of grid
    length = len(grid)

    # row index
    row_index = 0

    # column index
    col_index = 0

    for row in grid:
        # iterate through each cell
        for cell in row:
            print(cell)
            if cell == 1:
                sorround = 4
                # check if it get to the end of the row
                if row_index != breadth - 1:
                    if grid[row_index, col_index + 1] == 1:
                        sorround -= 1
                    if grid[row_index + 1, col_index] == 1:
                        sorround -= 1
                
