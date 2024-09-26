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

    # Initialize perimeter
    perimeter = 0

    for row in grid:
        # column index
        col_index = 0
        # iterate through each cell
        for cell in row:
            # if it a land area else skip
            if cell == 1:
                sorround = 4
                # check if it get to the end of the column
                if col_index != breadth - 1:
                    # check if next col has a cell
                    if grid[row_index][col_index + 1] == 1:
                        sorround -= 1
                # check if it is not the start of the column
                if col_index != 0:
                    # check if prev col has a cell
                    if grid[row_index][col_index - 1] == 1:
                        sorround -= 1
                # check if it get to the end of the row
                if row_index != length - 1:
                    # check if next row has a cell
                    if grid[row_index + 1][col_index] == 1:
                        sorround -= 1
                # check if it is not the start of the row
                if row_index != 0:
                    # check if prev row has a cell
                    if grid[row_index - 1][col_index] == 1:
                        sorround -= 1
                # add up the land perimeter
                perimeter += sorround
            col_index += 1
        row_index += 1

    return perimeter
