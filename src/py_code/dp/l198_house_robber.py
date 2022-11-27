from typing import List


def rob(nums: List[int]) -> int:
    N = len(nums)
    if N <= 2:
        return max(nums)
    dp = [0] * N
    dp[0] = nums[0]
    dp[1] = max(nums[:2])
    # dp = nums[:2]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # dp[i & 1] = max(dp[(i - 1) & 1], dp[i & 1] + nums[i])
    # return dp[(N - 1) & 1]
    return dp[N-1]

def robII(nums: List[int]) -> int:
    """
    House Robber II
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.

    All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
    Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
    adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
    can rob tonight without alerting the police.
    """
    def robAux(subnums):
        dp1, dp2 = 0, 0
        for num in subnums:
            # 注意此处对dp1, dp2 同时赋值，此时（1）dp1 = dp2还没有储存到disk中，
            # 因此 后面的（2）dp2 = max(dp1+num, dp2) 用的是上一次迭代的 dp1的值
            # 即 dp[N]   = max(dp[N-2]+nums[N], dp[N-1])
            # 即 dp_t[2] = max(dp_t-1[1]+nums[N], dp_t-1[2])
            #    dp_t[1] = dp_t-1[2]                          t是迭代的时间/步骤
            dp1, dp2 = dp2, max(dp1 + num, dp2)
        return dp2
    return max(robAux(nums[1:]), robAux(nums[:-1]))

def deleteAndEarn(nums: List[int]) -> int:
    """
    You are given an integer array nums. You want to maximize the number of points you get by performing the
    following operation any number of times:

    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1
    and every element equal to nums[i] + 1.

    Return the maximum number of points you can earn by applying the above operation some number of times.
    """
    max_val = max(nums)
    P = [0] * (max_val + 1)
    for num in nums:
        P[num] += num

    def rob():
        dp1, dp2 = 0, 0
        for i in range(1, max_val + 1):
            dp1, dp2 = dp2, max(dp1 + P[i], dp2)
        return dp2

    max_points = rob()
    return max_points

def deleteAndEarn2(nums: List[int]) -> int:
    nums.sort()

    def rob(array):
        dp1, dp2 = 0, 0
        for i in array:
            dp1, dp2 = dp2, max(dp1 + i, dp2)
        return dp2

    continuous_nums = [0]
    val = nums[0]
    max_points = 0
    for num in nums:
        if num == val:
            continuous_nums[-1] += num
        elif num == val + 1:
            continuous_nums.append(num)
            val = num
        else:
            max_points += rob(continuous_nums)
            val = num
            continuous_nums = [val]
    max_points += rob(continuous_nums)
    return max_points

def maxSizeSlices(slices: List[int]) -> int:
    """
    There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows: You
    will pick any pizza slice. Your friend Alice will pick the next slice in the anti-clockwise direction of your
    pick. Your friend Bob will pick the next slice in the clockwise direction of your pick. Repeat until there are no
    more slices of pizzas. Given an integer array slices that represent the sizes of the pizza slices in a clockwise
    direction, return the maximum possible sum of slice sizes that you can pick.

    HINT:
    等价于从3N个数里选择N个不相邻的数并且使之最大
    """
    N = len(slices)
    M = N // 3
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, i // 3 + 1):
            if i < 3:
                dp[i][j] = slices[i]
            dp[i][j] = max(dp[i - 2][j - 1] + slices[i], dp[i - 1][j])
    return dp[N][M]


if __name__ == "__main__":
    pizzas = [1, 2, 3, 4, 5, 6]
    maxSizeSlices(pizzas)