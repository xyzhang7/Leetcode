class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = list()
        nums.sort()

        for a in range(length):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b, c = a + 1, length - 1
            while b < c:
                total = nums[a] + nums[b] + nums[c]
                if total < 0:
                    b += 1
                elif total > 0:
                    c -= 1
                else:
                    while b < c and nums[b] == nums[b + 1]:
                        b += 1
                    while b < c and nums[c] == nums[c - 1]:
                        c -= 1
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
        return result
