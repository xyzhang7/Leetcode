"""
Given an array, arr[] of size N, the task is to count the number of pairs from the given array such that
the bitwise AND(&) of each pair is less than its bitwise XOR(^).
"""

from typing import List
import math
def cntPairs(arr: List[int]) -> int:
    res = 0
    bit = [0] * 32
    for i in range(0, len(arr)):
        pos = int(math.log(arr[i], 2))
        bit[pos] = bit[pos] + 1



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    N = len(arr)
    print(cntPairs(arr))
