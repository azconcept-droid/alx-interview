#!/usr/bin/python3
"""
This module minimum operation
"""


def minOperations(n):
    """ method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    Example:

    n = 9

    H => Copy All => Paste => HH => Paste =>HHH =>
    Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

    Number of operations: 6
    """

    # when n = 0 or 1
    if n == 0 or n == 1:
        return 0

    # when n = 2 only two operations
    if n == 2:
        return 2
    
    # when n = 3 only three operations
    if n == 3:
        return 3
