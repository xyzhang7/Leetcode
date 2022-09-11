import collections
from typing import List


def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    N = len(nums)
    if N <= 1:
        return False

    i = 0
    while i <= N - indexDiff:
        for l in range(1, indexDiff + 1):
            j = i + l
            if abs(nums[i] - nums[j]) <= valueDiff:
                return True
        i = i + 1
    return False


if __name__ == "__main__":
    containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)
    b = collections.Counter("aahfjaehfhli")
    b.most_common()
