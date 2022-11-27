def longestPalindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    def expand(i, j):
        while i >= 0 and j < n and s[i] == s[j]:
            i = i - 1
            j = j + 1
        return i+1, j-1

    l, r = 0, 0
    for p in range(n):
        l1, r1 = expand(p, p)
        l2, r2 = expand(p, p + 1)
        if r1 - l1 > r - l:
            l, r = l1, r1
        if r2 - l2 > r - l:
            l, r = l2, r2
    return s[l:r+1]


if __name__ == "__main__":
    s = "abbd"
    longestPalindrome(s)