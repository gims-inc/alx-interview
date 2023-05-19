#!/usr/bin/python3
"""Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to
    make change for the given amount.
    """
    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize the count of coins needed
    count = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Check if the coin can be used to make up the remaining total
        if coin <= total:
            # Calculate the number of coins needed for the current coin
            # denomination
            numCoins = total // coin
            count += numCoins

            # Update the remaining total
            total -= numCoins * coin

    # If there is still remaining total, it cannot be made up with the given
    # coin denominations
    if total != 0:
        return -1

    return count
