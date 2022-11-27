def numTrees(n: int) -> int:
    if n <= 1:
        return 1
    dp = [1 for _ in range(n)]

    for p in range(2, n+1):
        for i in range(1, p+1):
            dp[p] += dp[i-1] * dp[p-i]

# def numTrees(n: int) -> int:
#     """
#     Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#     """
#     dp = [[0] * n for _ in range(n)]
#
#     def recur(i, j):
#         if i == j:
#             dp[i][j] = 1
#             return
#
#         dp[i][j] += dp[i + 1][j] + dp[i][j - 1]
#         for k in range(i + 1, j):
#             dp[i][j] += dp[i][k - 1] * dp[k + 1][j]
#
#     recur(0, n - 1)
#     return dp[0][n - 1]


if __name__ == "__main__":
    n = 4
    numTrees(n)