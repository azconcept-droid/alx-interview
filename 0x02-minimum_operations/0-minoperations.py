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

    # Initialize the number of operations
    operations = 0

    # when n = 0 or 1 or negative
    if n == 0 or n == 1 or n < 0:
        return operations

    # when n >= 2
    # To get minimum operations to print 2 or more characters
    for number in range(2, n + 1):
        while n % number == 0:
            # Save the operation as you transverse
            operations += number
            # Reduce n by the number of times
            n = n // number
    
    return operations
