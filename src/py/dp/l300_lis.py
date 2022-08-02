"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""
from typing import List


def lengthOfLIS(self, nums: List[int]) -> int:
    N = len(nums)
    dp = [0] * N

    for i in range(0, N):
        for j in range(0, i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)