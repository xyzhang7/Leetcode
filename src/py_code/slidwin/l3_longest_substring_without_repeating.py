def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if not n:
        return 0

    l, r = 0, 0
    max_len, curr_len = 0, 0
    counter = set()
    while r < n:
        while s[r] in counter:
            counter.remove(s[l])
            l += 1
            curr_len -= 1
        counter.add(s[r])
        r += 1
        curr_len += 1
        max_len = max(max_len, curr_len)
    return max_len

if __name__ == '__main__':
    s = "pwwkew"
    lengthOfLongestSubstring(s)

