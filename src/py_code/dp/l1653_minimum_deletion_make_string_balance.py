import collections


def minimumDeletions(s: str) -> int:
    n = len(s)
    left, right = -1, n
    while left < n - 1 and s[left + 1] == 'a':
        left = left + 1
    while right > 0 and s[right - 1] == 'b':
        right = right - 1
    if left == n - 1 or right == 0 or left + 1 == right:
        return 0
    count = collections.Counter(s[left + 1:right])
    return min(count.values())


if __name__ == '__main__':
    s = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"
    minimumDeletions(s)