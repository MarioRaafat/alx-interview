#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coinIdx = 0
    counter = 0 
    remaining_coins = total

    while remaining_coins:
        if coinIdx == len(coins):
            return -1

        if remaining_coins >= sorted_coins[coinIdx]:
            remaining_coins -= sorted_coins[coinIdx]
            counter += 1
        else:
            coinIdx += 1
            continue

    return counter