from typing import List


def maxSubArray(nums: List[int]) -> int:
    N = len(nums)
    dp = nums[:]
    start = 0
    total = nums[0]

    for i in range(1, N):
        if dp[i - 1] > 0:
            dp[i] += dp[i - 1]
        else:
            start = i
        if dp[i] > total:
            total = dp[i]

    return total

def maxSubArrayAns(self, nums: List[int]) -> int:
    pre = 0
    maxAns = nums[0]

    for i in nums:
        pre = max(0, pre + i)
        maxAns = max(pre, maxAns)

    return maxAns


if __name__ == "__main__":
    maxSubArrayAns([-2,1,-3,4,-1,2,1,-5,4])