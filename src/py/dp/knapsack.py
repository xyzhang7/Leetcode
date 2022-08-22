from typing import List


def fractional_knapsack(weights: List[int], values: List[int], W: int) -> int:
    """
    01 Knapsack problem. The greedy algorithm does not work A thief robbing a store finds n items. The ith item is
    worth vi dollars and weighs wi pounds, where 􏰁i and wi are integers. The thief wants to take as valuable a load
    as possible, but he can carry at most W pounds in his knapsack, for some integer W .
    :param weights: weight of each item
    :param values: value of each item
    :param W: maximum weight the thief can carry
    :return: maximum value thr thief can get given the limit of W
    """
    N = len(values)
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(1, W+1):
            v1 = dp[i-1][w]
            v2 = dp[i-1][w-weights[i-1]] + values[i-1] if w >= weights[i-1] else 0
            dp[i][w] = max(v1, v2)
    print(dp)
    return dp[N][W]

def fractional_knapsack_o1space(weights: List[int], values: List[int], W: int) -> int:
    """
    O: O(NW) -> O(W)
    """
    N = len(values)
    dp = [0] * (W+1)
    for i in range(N):
        for w in range(W, weights[i]-1, -1):
            v1 = dp[w]
            v2 = dp[w - weights[i]] + values[i]
            dp[w] = max(v1, v2)
    return dp[W]

def canPartition_knapsack(nums: List[int]) -> bool:
    """
    LC 416 Given a non-empty array nums containing only positive integers, find if the array can be partitioned into
    two subsets such that the sum of elements in both subsets is equal.
    Note: partial knapsack problem -
    - maximum weight should be *no larger than* W
    - convert the problem to knapsack: let both the value[i] and weight[i] be nums[i]
    """
    SUM = sum(nums)
    if SUM & 1:
        return False

    HALF = SUM >> 1
    N = len(nums)
    dp = [[0] * (HALF + 1)]
    for i in range(N):
        for j in range(HALF, nums[i] - 1, -1):
            v1 = dp[j]
            v2 = dp[j - nums[i]] + nums[i]
            dp[j] = max(v1, v2)
    return dp[HALF] == HALF

def canPartition_knapscak_bool(nums: List[int]) -> bool:
    """
    Note: partial knapsack problem
    - dp = [bool] * target  => total weight is *exactly* half of the SUM
    """
    N = len(nums)
    total = sum(nums)
    if total & 1:
        return False

    half = total >> 1
    dp = [[False] * (half + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(half + 1):
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[N][half]

def complete_knapsack(weights: List[int], values: List[int], W: int) -> int:
    """
    Complete Knapsack problem. The greedy algorithm does not work. The ith item CAN BE TAKEN MULTIPLE TIMES, and its
    worth vi dollars and weighs wi pounds, where vi and wi are integers. The thief wants to take as valuable a load
    as possible, but he can carry at most W pounds in his knapsack, for some integer W .
    :param weights: weight of each item
    :param values: value of each item
    :param W: maximum weight the thief can carry
    :return: maximum value thr thief can get given the limit of W
    """
    N = len(values)


if __name__ == "__main__":
    canPartition_knapscak_bool([100])

