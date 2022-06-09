class Solution:
    def quicksort(self, nums):
        if not nums:
            return nums
        pivot = nums[0]
        left, right, middle = [], [], []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
        return self.quicksort(left) + middle + self.quicksort(right)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = list()
        sorted_nums = self.quicksort(nums)

        for a in range(length):
            if a > 0 and sorted_nums[a] == sorted_nums[a-1]:
                continue
            b, c = a + 1, length - 1
            while b < c:
                total = sorted_nums[a] + sorted_nums[b] + sorted_nums[c]
                if total < 0 or (b > a + 1 and sorted_nums[b] == sorted_nums[b-1]):
                    b += 1
                elif total > 0:
                    c -= 1
                else:
                    result.append([sorted_nums[a], sorted_nums[b], sorted_nums[c]])
                    b += 1
                    c -= 1
        return result
            
