from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    """
    Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order.
    """
    n = len(nums)
    ans = []

    def recur(first, nums):
        if first == n - 1:
            ans.append(nums[:])
            return

        recur(first + 1, nums)

        for i in range(first + 1, n):
            if nums[i] == nums[first]:
                continue
            nums[i], nums[first] = nums[first], nums[i]
            recur(first + 1, nums)
            nums[i], nums[first] = nums[first], nums[i]

    recur(0, nums)
    return ans

if __name__ == '__main__':
    permuteUnique([1, 1, 2, 2])