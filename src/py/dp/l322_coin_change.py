from typing import List

"""You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money. 

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1. 

You may assume that you have an infinite number of each kind of coin.
"""


def coinChange(coins: List[int], amount: int) -> int:
    N = len(coins)
    MAX = amount + 1
    dp = [[MAX] * (amount + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(amount + 1):
            dp[i][j] = dp[i - 1][j]

            k = 1
            while k * coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - k * coins[i - 1]] + k)
                k += 1
    return dp[N][amount]


def coinChange_optimal(coins: List[int], amount: int) -> int:
    MAX = amount
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
        dp[i] = min([MAX] + [1 + dp[i - c] for c in coins if i >= c])

    if dp[amount] == MAX:
        return -1

    return dp[amount]


if __name__ == "__main__":
    coinChange([1, 2, 5], 3)