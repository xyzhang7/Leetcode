"""
LeetCode Weekly Contest 310
"""
def largestCountValue(a):
    # Write your code here
    N = len(a)
    ans = 0
    if N < 2:
        return ans

    def merge_cnt(left, right):
        cnt = 0
        if left < right:
            q = (left + right) // 2
            cnt = 1 if min(a[left:q + 1]) < max(a[q + 1:right + 1]) else 0
            cnt += merge_cnt(left, q)
            cnt += merge_cnt(q + 1, right)
        return cnt

    return merge_cnt(0, N - 1)

def partitionString(s: str) -> int:
    frequencies = [set(s[0])]
    for c in s:
        if c in frequencies[-1]:
            frequencies.append(set(c))
        else:
            frequencies[-1].add(c)
    return len(frequencies)

from typing import List
def minGroups(intervals: List[List[int]]) -> int:
    groups = [[intervals[0]]]
    N = 1

    for i in intervals[1:]:
        merged = False
        k = 0
        while k < N:
            can_merge = True
            j = 0
            while j < len(groups[k]):
                if i[1] < groups[k][j][0] or i[0] > groups[k][j][1]:
                    j = j + 1
                    continue
                else:
                    can_merge = False
                    break
            if not can_merge:
                k = k + 1
                continue
            else:
                groups[k].append(i)
                merged = True
                break
        if not merged:
            groups.append([intervals[0]])
            N += 1
    return N

if __name__ == "__main__":
    largestCountValue([6, 1, 2, 3, 4, 5, 10])
    minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]])