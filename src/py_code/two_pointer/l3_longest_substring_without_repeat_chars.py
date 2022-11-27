def lengthOfLongestSubstring(s: str) -> int:
    left = right = 0
    cur = res = 0
    index_map = dict()

    while right < len(s):
        if s[right] not in index_map:
            index_map[s[right]] = right
            cur += 1
            res = max(res, cur)
        else:
            left = index_map[s[right]] + 1
            index_map[s[right]] = right
            cur = right - left + 1
        right += 1

    return res

def lengthOfLongestSubstringAns(s: str) -> str:
    ans = 0
    mp = {}      # mp store the current index of the character
    i, j = 0, 0  # i, j is the left and right pointer of sliding window
    for j in range(len(s)):
        if s[j] in mp:
            i = max(mp[s[j]], i)
    reversed("abc")


if __name__ == "__main__":
    lengthOfLongestSubstring("tmmzuxt")