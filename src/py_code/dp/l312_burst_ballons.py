from typing import List
import math
"""You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an 
array nums. You are asked to burst all the balloons. 

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of 
bounds of the array, then treat it as if there is a balloon with a 1 painted on it. 

Return the maximum coins you can collect by bursting the balloons wisely.

NOTE: If you think of bursting a balloon as multiplying two adjacent matrices, then this problem is exactly the 
classical DP problem Matrix-chain multiplication found in section 15.2 in the book Introduction to Algorithms (2nd 
edition). 

For example, given [3,5,8] and bursting 5, the number of coins you get is the number of scalar multiplications you 
need to do to multiply two matrices A[3*5] and B[5*8]. So in this example, the original problem is actually the same 
as given a matrix chain A[1*3]*B[3*5]*C[5*8]*D[8*1], fully parenthesize it so that the total number of scalar 
multiplications is maximized, although the orignal matrix-chain multiplication problem in the book asks to minimize 
it. Then you can see it clearly as a classical DP problem. """


def maxCoins(nums: List[int]) -> int:
    ballons = [1] + [n for n in nums if n > 0] + [1]
    N = len(ballons)
    dp = [[0] * N for _ in range(N)]

    for l in range(1, N+1):
        for i in range(0, N-l+1):
            j = l + i - 1
            for k in range(i+1, j):
                temp = dp[i][k] + dp[k][j] + ballons[i] * ballons[k] * ballons[j]
                if temp > dp[i][j]:
                    dp[i][j] = temp
    return dp[0][N-1]

def matrixMultiplication(nums: List) -> int:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(0, n-l+1):
            j = i + l - 1
            dp[i][j] = math.inf
            for k in range(i, j):
                p = dp[i][k] + dp[k+1][j] + nums[i][0] * nums[k][1] * nums[j][1]
                if p < dp[i][j]:
                    dp[i][j] = p
                    s[i][j] = k
    return dp[0][n-1]


if __name__ == "__main__":
    nums = [3, 1, 5, 8]
    # nums = [1, 5, 8, 7, 4, 3]
    # matrices = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
    # matrixMultiplication(matrices)
