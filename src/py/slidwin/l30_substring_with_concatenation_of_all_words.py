import collections
from typing import List


def findSubstring(s: str, words: List[str]) -> List[int]:
    ans = []
    if not words or not s or not words[0]:
        return ans

    M, L = len(words), len(words[0])
    N = len(s)
    if N < M * L:
        return ans

    p = 0
    while p < N:
        if s[p:p + L] not in words:
            p = p + 1
        else:
            cur_index = words[:]
            prev = p
            while p < N:
                if s[p:p + L] in cur_index:
                    cur_index.remove(s[p:p + L])
                    if not cur_index:
                        ans.append(prev)
                        break
                    p = p + L
                else:
                    break
            p = prev + 1
    return []

def findSubstringSlidingWindow(s: str, words: List[str]) -> List[int]:
    n, k = len(s), len(words)
    if not n or not k or not words[0]:
        return None

    word_length = len(words[0])
    words_count = collections.Counter(words)
    ans = []

    def slidingWindow(left):
        words_found = collections.defaultdict(int)
        words_used = 0
        right = left
        while right <= n - word_length:
            sub = s[right: right + word_length]
            if sub in words_count:
                words_found[sub] += 1
                words_used += 1
                while words_found[sub] > words_count[sub]:
                    left_sub = s[left: left + word_length]
                    words_found[left_sub] -= 1
                    words_used -= 1
                    left = left + word_length
                if words_used == k:
                    ans.append(left)
                right = right + word_length
            else:
                # If we encounter a word not in the words, reset the counter
                left = right = right + word_length
                words_found = collections.defaultdict(int)
                words_used = 0

    for i in range(word_length):
        slidingWindow(i)
    return ans


def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    if indexDiff < 1 or valueDiff < 0:
        return False
    dic = collections.OrderedDict()
    for n in nums:
        key = n if not valueDiff else n // valueDiff
        for m in (dic.get(key), dic.get(key-1), dic.get(key+1)):
            if m is not None and abs(n - m) <= valueDiff:
                return True
            if len(dic) == indexDiff:
                # first in first out, pop the oldest item in dic
                dic.popitem(False)
            dic[key] = n
    return False


if __name__ == "__main__":
    containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
    # findSubstringSlidingWindow("dddddddddddd", ["dddd","dddd"])
    # findSubstringSlidingWindow("aaa", ["a","a"])
    # findSubstringSlidingWindow("barfoothefoobarman", ["foo","bar"])
    # findSubstringSlidingWindow("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])