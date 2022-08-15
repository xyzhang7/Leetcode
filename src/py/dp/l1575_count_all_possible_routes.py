from collections import defaultdict
from typing import List


def countRoutes(locations: List[int], start: int, finish: int, fuel: int) -> int:
    """
    You are given an array of distinct positive integers locations where locations[i] represents the position of city
    i. You are also given integers start, finish and fuel representing the starting city, ending city,
    and the initial amount of fuel you have, respectively.

    At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and
    move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[
    j]|. Please notice that |x| denotes the absolute value of x.

    Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more
    than once (including start and finish).

    Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo
    109 + 7.

    NOTE: top-down approach + memorization
    """
    N = len(locations)
    cache = [[-1] * (fuel + 1) for _ in range(N)]
    for i in range(N):
        if i != finish:
            cache[i][0] = 0
        else:
            cache[i][0] = 1

    def dfs(src, f):
        if cache[src][f] != -1:
            return cache[src][f]

        if abs(locations[finish] - locations[src]) > fuel:
            cache[src][f] = 0
            return 0

        num_routes = 0
        if src == finish:
            num_routes = 1

        for s in range(N):
            cost = abs(locations[s] - locations[src])
            if s != src and f >= cost:
                num_routes += dfs(s, f - cost)
        return num_routes

    return dfs(start, fuel)



def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    """
    LC 576
    There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are
    allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the
    grid boundary). You can apply at most maxMove moves to the ball.

    Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of
    the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
    """
    dp = defaultdict(list)

    def solve(i, j, maxMove, memo):
        if (i, j, maxMove) in memo:
            return memo[(i, j, maxMove)]

        if maxMove < 0:
            return 0

        if i < 0 or i >= m or j < 0 or j >= n:
            return 1

        a = solve(i - 1, j, maxMove - 1, memo)
        b = solve(i + 1, j, maxMove - 1, memo)
        c = solve(i, j - 1, maxMove - 1, memo)
        d = solve(i, j + 1, maxMove - 1, memo)

        memo[(i, j, maxMove)] = a + b + c + d

        return memo[(i, j, maxMove)]

    return solve(startRow, startColumn, maxMove, dp) % 1000000007


from itertools import product

def findPathsDP(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    """
    LC 576 DP
    T: O(mn * maxMove)
    S: O(mn)
    """
    if maxMove == 0: return 0
    dpCurr = [[0] * (n+2) for _ in range(m+2)]
    dpLast = [[0] * (n+2) for _ in range(m+2)]
    for i in range(1, m+1):
        dpCurr[i][1] += 1
        dpCurr[i][n] += 1
    for j in range(1, n+1):
        dpCurr[1][j] += 1
        dpCurr[m][j] += 1
    ans = dpCurr[startRow+1][startColumn+1]
    for d in range(maxMove-1):
        dpCurr, dpLast = dpLast, dpCurr
        for i, j in product(range(1, m+1), range(1, n+1)):
            dpCurr[i][j] = (dpLast[i-1][j] + dpLast[i+1][j] + dpLast[i][j-1] + dpLast[i][j+1]) % 1000000007
        ans = (ans + dpCurr[startRow+1][startColumn+1]) % 1000000007
    return ans


if __name__ == "__main__":
    findPathsImpl(3, 4, 3, 0, 0)
