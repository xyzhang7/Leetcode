def longestPalindrome(s: str) -> str:
    N = len(s)
    dp = [[0] * N for _ in range(N)]
    start = None
    length = 1

    for l in range(1, N + 1):
        for i in range(0, N - l + 1):
            j = l + i - 1
            if l == 1:
                dp[i][j] = 1
                continue
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
                if dp[i][j] > length:
                    start = i
                    length = dp[i][j]
    return s[start:start + length]


def longestPalindromeTwoPointer(s: str) -> str:
    N = len(s)
    start, length = 0, 1

    def expandAroundCenter(i, j):
        while i >= 0 and j < N and s[i] == s[j]:
            i = i - 1
            j = j + 1
        return j - i - 1

    for n in range(N):
        len1 = expandAroundCenter(n, n)
        if len1 > length:
            start = int(n - (len1 - 1) / 2)
            length = len1
        if n < N - 1:
            len2 = expandAroundCenter(n, n + 1)
            if len2 > length:
                start = n - int(len2/2) + 1
    return s[start:start+length]

if __name__ == "__main__":
    # longestPalindrome("abad")
    longestPalindromeTwoPointer("aaa")
    # print(longestPalindromeTwoPointer("aacabdkacaa"))