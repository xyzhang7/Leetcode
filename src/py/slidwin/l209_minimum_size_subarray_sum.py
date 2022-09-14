from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    N = len(nums)
    ans = N + 1
    left = right = 0
    curr = 0
    curr_sum = 0

    while right < N:
        curr_sum += nums[right]
        right += 1
        curr += 1
        while curr_sum >= target:
            if curr < ans:
                ans = curr
            curr_sum -= nums[left]
            curr -= 1
            left += 1
    return 0 if ans == N + 1 else ans

if __name__ == "__main__":
    minSubArrayLen(7, [2,3,1,2,4,3])