from typing import List

def binarySearch(nums: List[int], target) -> int:
    """
    算法：* 闭区间，* 找不到返回 -1
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        ### mid = (left + right) // 2 may cause int overflow
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left = mid + 1
        elif nums[mid] < target:
            right = mid - 1
    return -1

def binarySearchLeftBound(nums: List[int], target):
    """
    假设 nums 中有很多target，返回最左边的值
    """
    pass

