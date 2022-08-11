"""
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3 xi + xi+1 == xi+2 for all i + 2 <= n Given a strictly increasing array arr of positive integers forming a
sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr,
without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""
from typing import List


def lenLongestFibSubseq(A):
    """
    Brute force
    """
    S = set(A)
    ans = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            """
            With the starting pair (A[i], A[j]),
            y represents the future expected value in
            the fibonacci subsequence, and x represents
            the most current value found.
            """
            x, y = A[j], A[i] + A[j]
            length = 2
            while y in S:
                x, y = y, x + y
                length += 1
            ans = max(ans, length)
    return ans if ans >= 3 else 0


def lenLongestFibSubseqDP(arr: List[int]) -> int:
    """
    DP:
    if arr[k] + arr[i] == arr[j]:
        dp[i][j] = max(dp[k][i] + 1) for k in range(0, i)
    """
    N = len(arr)
    ans = 0
    dp = [[2] * (N) for _ in range(N)]

    for i in range(1, N):
        for j in range(i + 1, N):
            if j >= i * i:
                break
            for k in range(i):
                if arr[k] + arr[i] == arr[j]:
                    dp[i][j] = max(dp[k][i] + 1, dp[i][j])

            ans = max(ans, dp[i][j])
    return ans


if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8]
    lenLongestFibSubseqDP(A)