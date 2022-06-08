class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low, high]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [numbers[low], numbers[high]]
