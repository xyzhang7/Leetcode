"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
"""


def countSubstrings(s: str) -> int:
    N = len(s)
    dp = [0] * N

    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [0] * N

        def countSubstringsAux(i, j):
            temp = 0
            while i >= 0 and j < N and s[i] == s[j]:
                temp += 1
                i -= 1
                j += 1
            return temp

        for n in range(N):
            dp[n] = countSubstringsAux(n, n) + countSubstringsAux(n, n + 1)
        return sum(dp)


if __name__ == "__main__":
    s = "abc"
    countSubstrings(s)
