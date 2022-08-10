"""
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3 xi + xi+1 == xi+2 for all i + 2 <= n Given a strictly increasing array arr of positive integers forming a
sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr,
without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""


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


if __name__ == "__main__":
    A = [2,4,7,8,9,10,14,15,18,23,32,50]
    lenLongestFibSubseq(A)