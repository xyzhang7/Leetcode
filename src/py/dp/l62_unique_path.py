import heapq
from typing import List

n = 0

def minPathSum(grid: List[List[int]]) -> int:
    """
    LC 64 Minimum Path Sum Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
    right, which minimizes the sum of all numbers along its path.
    Note1: You can only move either down or right at any point in time.
    """
    m, n = len(grid), len(grid[0])
    dp = grid[:]
    for i in range(m):
        for j in range(n):
            if i >= 1 and j >= 1:
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
            elif i >= 1:
                dp[i][j] += dp[i - 1][j]
            elif j >= 1:
                dp[i][j] += dp[i][j - 1]

    return dp[m - 1][n - 1]


def minPath(grid: List[List[int]]) -> int:
    """
    LC 64 -> print the minimum path (if there are multiple, print only one of them
    """
    m, n = len(grid), len(grid[0])
    MAX = float("inf")

    def getIdx(x, y):
        return x * n + y

    def parseIdx(idx):
        return [idx // n, idx % n]

    dp = grid[:]
    minPathIdx = dict()

    # generate min path by dp
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            top = dp[i - 1][j] if i >= 1 else MAX
            left = dp[i][j - 1] if j >= 1 else MAX
            dp[i][j] += min(top, left)
            minPathIdx[getIdx(i, j)] = getIdx(i-1, j) if top < left else getIdx(i, j-1)

    # parse the min path index into (i, j)
    minPath = [[0] * 2 for _ in range(m+n)]
    minPath[-1] = [m-1, n-1]
    last = getIdx(m-1, n-1)
    for i in range(m+n-2, 0, -1):
        minPath[i] = parseIdx(minPathIdx[last])
        last = minPathIdx[last]

    # print the min path
    for i in range(1, m+n):
        x, y = minPath[i]
        print(f"({x}, {y})")
    print()


def minimumTotal(triangle: List[List[int]]) -> int:
    N = len(triangle)
    if N == 1:
        return triangle[0][0]

    dp = [0] * N
    ans = float("inf")
    for i in range(N):
        for j in range(i, -1, -1):
            if j == 0:
                dp[j] += triangle[i][j]
            elif j == i:
                dp[j] = dp[j - 1] + triangle[i][j]
            else:
                dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]

            if i == N - 1:
                ans = min(dp[j], ans)
    return ans

def minFallingPathSum(matrix: List[List[int]]) -> int:
    N = len(matrix)
    if N == 1:
        return matrix[0][0]

    MAX = float("inf")
    dp = [[0] * N for _ in range(2)]
    dp[0] = matrix[0][:]
    ans = MAX

    for i in range(1, N):
        for j in range(N):
            diagonal_left = dp[(i - 1) & 1][j - 1] if j > 0 else MAX
            diagonal_right = dp[(i - 1) & 1][j + 1] if j < N - 1 else MAX
            dp[i & 1][j] = min(diagonal_left, dp[(i - 1) & 1][j], diagonal_right) + matrix[i][j]

            if i == N - 1:
                ans = min(ans, dp[i & 1][j])
    return ans

def minFallingPathSum2(grid: List[List[int]]) -> int:
    """
    Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

    A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two
    elements chosen in adjacent rows are in the same column.

    Improve the time complexity to O(N^2) by save the two smallest number in previous row
    T: O(N^2)
    S: O(N)
    """
    N = len(grid)
    dp = [[0] * N for _ in range(2)]
    dp[0] = grid[0][:]
    two_smallest = heapq.nsmallest(2, dp[0])

    for i in range(1, N):
        for j in range(N):
            if dp[(i - 1) & 1][j] == two_smallest[0]:
                dp[i & 1][j] = two_smallest[1] + grid[i][j]
            else:
                dp[i & 1][j] = two_smallest[0] + grid[i][j]
            two_smallest = heapq.nsmallest(2, dp[i & 1])

    return min(dp[(N - 1) & 1])

if __name__ == "__main__":

    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    heapq.nsmallest(2, matrix[0])
    minFallingPathSum(matrix)
