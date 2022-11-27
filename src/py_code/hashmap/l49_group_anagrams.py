import collections
from typing import List

def groupAnagrams_sort_and_compare(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

def groupAnagrams_categorize_by_count(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

if __name__ == '__main__':
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])