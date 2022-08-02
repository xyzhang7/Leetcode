from typing import List

"""You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money. 

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1. 

You may assume that you have an infinite number of each kind of coin.
"""


def coinChange(coins: List[int], amount: int) -> int:
    MAX = amount
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
        dp[i] = min([MAX] + [1 + dp[i - c] for c in coins if i >= c])

    if dp[amount] == MAX:
        return -1

    return dp[amount]


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))