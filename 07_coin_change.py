"""
DSA Lab: Making a Change Problem (Coin Change) using Dynamic Programming
Given a set of coin denominations and a target amount, find the minimum
number of coins needed to make that amount (and the coins used).
"""

import time


def coin_change_min_coins(coins, amount):
    """
    coins: list of coin denominations
    amount: target amount
    Returns: (min_coins, coins_used) or (-1, []) if not possible
    """
    # dp[i] = minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # coin_used[i] = coin used to reach amount i optimally
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return -1, []

    # Reconstruct which coins were used
    result = []
    curr = amount
    while curr > 0:
        result.append(coin_used[curr])
        curr -= coin_used[curr]

    return dp[amount], result


def count_ways_to_make_change(coins, amount):
    """
    Bonus: counts the number of distinct ways to make the amount
    (unbounded knapsack style DP), useful for comparison.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50]
    amount = 93

    start = time.time()
    min_coins, coins_used = coin_change_min_coins(coins, amount)
    end = time.time()

    print(f"Coin denominations: {coins}")
    print(f"Target amount: {amount}")

    if min_coins == -1:
        print("It is not possible to make this amount with the given coins.")
    else:
        print(f"Minimum number of coins required: {min_coins}")
        print(f"Coins used: {coins_used}")

    ways = count_ways_to_make_change(coins, amount)
    print(f"Total number of distinct ways to make the amount: {ways}")
    print(f"Time taken: {end - start:.6f} seconds")