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

def findNumberOfLIS(nums: List[int]) -> int:
    N = len(nums)
    dp = [1] * N
    counts = [1] * N

    for i in range(1, N):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 == dp[i]:
                counts[i] += counts[j]
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                counts[i] = counts[j]

    max_length = 0
    max_counts = 0
    for i in range(N):
        if dp[i] > max_length:
            max_length = dp[i]
            max_counts = counts[i]

    return max_counts

def maxSubarraySumCircular(nums: List[int]) -> int:
    """
    Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
    """
    N = len(nums)
    max_right = [0] * (N+1)
    max_right[N-1] = nums[N-1]
    for i in range(N - 2, -1, -1):
        # cumulative sum of nums[i:]
        max_right[i] += max_right[i + 1] + nums[i]

    for i in range(N - 2, -1, -1):
        # calculate the maximum sum in range nums[i:]
        #     i.e., the range is nums[j:N-1], where j <= i
        max_right[i] = max(max_right[i + 1], max_right[i])

    leftsum, pre, curmax = 0, 0, -float("inf")
    for i in range(N):
        # max subarray sum is cumulative sum of left part sum(nums[0:i]) +
        #     max_right[i+1]
        pre = nums[i] + max(0, pre)
        curmax = max(pre, curmax, leftsum + nums[i] + max_right[i+1])
        leftsum += nums[i]


def maxSubarraySumCircular2( nums: List[int]) -> int:
    """
    Explanation
So there are two case.
Case 1. The first is that the subarray take only a middle part, and we know how to find the max subarray sum.
Case2. The second is that the subarray take a part of head array and a part of tail array.
We can transfer this case to the first one.
The maximum result equals to the total sum minus the minimum subarray sum.

    Corner case
Just one to pay attention:
If all numbers are negative, maxSum = max(A) and minSum = sum(A).
In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
According to the deacription, We need to return the max(A), instead of sum of am empty subarray.
So we return the maxSum to handle this corner case.
    """
    N = len(nums)
    array_sum = 0
    premax, premin = 0, 0
    curmax, curmin = -float("inf"), float("inf")
    for i in range(N):
        premax = nums[i] + max(premax, 0)
        curmax = max(curmax, premax)
        premin = nums[i] + min(premin, 0)
        curmin = min(curmin, premin)
        array_sum += nums[i]
    if array_sum == curmin:
        return curmax
    return max(curmax, array_sum - curmin)

if __name__ == "__main__":
    maxSubarraySumCircular2([-3, -2, -3])