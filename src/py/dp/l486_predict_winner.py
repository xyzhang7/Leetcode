from typing import List


def PredictTheWinner1(nums: List[int]) -> bool:
    """
    You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

    Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At
    each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length -
    1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends
    when there are no more elements in the array.

    Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the
    winner, and you should also return true. You may assume that both players are playing optimally.
    """
    N = len(nums)
    if N & 1 == 0:
        return True

    dp = [[0] * N for _ in range(N)]
    for L in range(1, N + 1):
        for i in range(0, N):
            j = i + L - 1
            if j >= N:
                break

            if L == 1:
                dp[i][j] = nums[i]
                continue

            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

    return dp[0][N - 1] >= 0


def PredictTheWinner2(nums: List[int]) -> bool:
    """
    优化上一步算法
    T: O(n^2)
    S: O(n^2) -> O(n)
    """
    N = len(nums)
    # if N & 1 == 0:
    #     return True
    dp = [0 for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(i, N):
            if i == j:
                dp[i] = nums[i]
            else:
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
    return dp[N-1] >= 0


if __name__ == "__main__":
    nums = [1, 5, 2, 7]
    PredictTheWinner2(nums)