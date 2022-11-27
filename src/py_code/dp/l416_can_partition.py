from typing import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total & 1:
        return False

    target = total >> 1
    dp = [False] * (target + 1)
    dp[0] = True
    for i in nums:
        for j in range(target, i-1, -1):
            dp[j] = dp[j] or dp[j-i]
    return dp[target]


if __name__ == "__main__":
    canPartition([1, 5, 11, 5])