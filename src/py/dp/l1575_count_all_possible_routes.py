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

def pathsWithMaxScore(board: List[str]) -> List[int]:
    """
    LC1301 Number of Paths with Max Score
    You are given a square board of characters. You can move on the board starting at the bottom right square marked
    with the character 'S'.

    You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either
    with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (
    diagonally) only if there is no obstacle there.

    Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect,
    and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

    In case there is no path, return [0, 0].
    """
    N = len(board)

    def to_num(grid):
        start_char, end_char, obstacle_char = 'S', 'E', 'X'
        if grid == start_char or grid == end_char:
            return 0
        elif grid == obstacle_char:
            return -1
        elif '1' <= grid <= '9':
            return int(grid)
        else:
            return -2

    # numeric board store the max value gaid from starting point to each grid
    numeric_board = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            numeric_board[i][j] = to_num(board[i][j])
            if numeric_board[i][j] == -2:
                return [0, 0]

    # dp store the number of paths from starting point to each grid
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[N-1][N-1] = 1

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if (i == N - 1 and j == N - 1) or numeric_board[i][j] == -1:
                continue

            curr_max = max(numeric_board[i][j + 1], numeric_board[i + 1][j], numeric_board[i + 1][j + 1])
            if curr_max == -1:
                continue

            numeric_board[i][j] += curr_max
            if numeric_board[i][j + 1] == curr_max:
                dp[i][j] += dp[i][j + 1]
            if numeric_board[i + 1][j] == curr_max:
                dp[i][j] += dp[i + 1][j]
            if numeric_board[i + 1][j + 1] == curr_max:
                dp[i][j] += dp[i + 1][j + 1]
    if dp[0][0] == 0:
        return [0, 0]
    return [numeric_board[0][0], dp[0][0]]


def pathsWithMaxScoreSol(board):
    """
    LC 1301 Best and most elegant solution @lee215
    T: O(n^2), S: O(n^2)
    """
    n, mod = len(board), 10**9 + 7

    # dp[x][y][0] is the maximum value to this cell,
    # dp[x][y][1] is the number of paths.
    dp = [[[-10**5, 0] for j in range(n+1)] for i in range(n+1)]
    dp[n-1][n-1] = [0, 1]
    for x in range(n)[::-1]:
        for y in range(n)[::-1]:
            if board[x][y] in 'XS': continue
            for i, j in [[0, 1], [1, 0], [1, 1]]:
                if dp[x][y][0] < dp[x+i][y+j][0]:
                    dp[x][y] = [dp[x+i][y+j][0], 0]
                if dp[x][y][0] == dp[x+i][y+j][0]:
                    dp[x][y][1] += dp[x+i][y+j][1]

            # add the board number in grid [x, y] if it is not the 'end' cell
            dp[x][y][0] += int(board[x][y]) if x or y else 0

    # if the number of maximum ways from start to end is 0, then return [0, 0]
    return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % mod]



if __name__ == "__main__":
    board1 = ["E23","2X2","12S"]
    board2 = ["E11","XXX","11S"]
    pathsWithMaxScore(board1)
