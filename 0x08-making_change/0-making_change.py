#!/usr/bin/python3

"""This programs determines the fewest number of coins needed to meet a
given amount total, given a pile of coins of different values.
"""


def makeChange(coins, total):
    """Function to make change"""
    if total <= 0:
        return 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    # Fill DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check the result
    return dp[total] if dp[total] != float('inf') else -1
