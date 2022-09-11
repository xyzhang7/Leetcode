def largestCountValue(a):
    # Write your code here
    N = len(a)
    if N < 2:
        return 0

    def merge_cnt(left, right):
        cnt = 0
        if left < right:
            q = (left + right) // 2
            cnt = 1 if max(a[left:q + 1]) > min(a[q + 1:right + 1]) else 0
            cnt += merge_cnt(left, q)
            cnt += merge_cnt(q + 1, right)
        return cnt

    return merge_cnt(0, N - 1)

if __name__ == "__main__":
    print(largestCountValue([3, 1, 4, 2, 5]))