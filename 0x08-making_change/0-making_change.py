#!/usr/bin/python3
"""Contains function for fewer changes
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed
       to meet a given amount total."""
    if total <= 0:
        return 0

    # Initialize dp array with infinity
    # for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Process each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, we return -1 because
    # it's not possible to make that amount
    return dp[total] if dp[total] != float('inf') else -1
