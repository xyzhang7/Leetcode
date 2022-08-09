from math import ceil, log2

class SegmentTree:
    def __init__(self, array):
        """
        construct a segment tree from a given array arr
        """
        N = len(array)
        self.height = ceil(log2(N))
        self.segmentTree = [0] * (2 * 2 ** self.height)
        # self.recur_build(array, 0, N - 1, 0)
        self.build(array)

    def build(self, array):
        """
        func that builds segment tree for array.
        Similar to the func `recur_build`
        这里将segment tree的第一位空出来方便计数
        """
        N = len(array)
        for i in range(N):
            self.segmentTree[N + i] = array[i]
        for i in range(N-1, 0, -1):
            self.segmentTree[i] = self.segmentTree[i << 1] + self.segmentTree[i << 1 | 1]

    def recur_build(self, array, l, r, idx):
        """
        a recursive func that constructs segment tree for array[l:r]
        :param idx: index of current node in segment tree st
        """
        if l == r:
            self.segmentTree[idx] = array[l]
            return array[l]
        mid = l + (r - l) // 2
        self.segmentTree[idx] = self.recur_build(array, l, mid, idx * 2 + 1) + \
                                self.recur_build(array, mid + 1, r, idx * 2 + 2)
        return self.segmentTree[idx]

    def modify(self, p, N, value):
        """
        set the value at position array[p]
        """
        self.segmentTree[p + N] = value
        while p > 1:
            self.segmentTree[p >> 1] = self.segmentTree[p] + self.segmentTree[p ^ 1]
            p = p >> 1

    def query(self, l, r, N):
        """
        query sum on interval [l, r]
        """
        res = 0
        l += N
        r += N
        while l < r:
            if l & 1:
                res += self.segmentTree[l]
                l = l + 1
            if r & 1:
                r = r - 1
                res += self.segmentTree[r]
            l = l >> 1
            r = r >> 1

    def range_sum(self, l, r):
        """
        a recursive func to get the sum of values in the given range of the array.
        :param l:
        :param r:
        :return:
        """
        pass

if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9, 11]
    arr2 = [i+1 for i in range(4)]
    st = SegmentTree(arr2)
