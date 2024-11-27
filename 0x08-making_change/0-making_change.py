#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

    Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of coin in the list
    Your solution’s runtime will be evaluated in this task

"""


def makeChange(coins, total):
    """ determine fews amount of coin to meet the
    the given total amount
    """
    n = len(coins)
    if total <= 0:
        return 0
    if n == 0:
        return -1
    db = [[0 for x in range(total+1)] for x in range(n+1)]

    for i in range(n+1):
        db[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            db[i][j] = db[i - 1][j]
            if j >= coins[i - 1]:
                db[i][j] += db[i][j - coins[i - 1]]

    return db[n][total]
