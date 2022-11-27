class MedianFinder:
    def __init__(self, num):
        self.median = None
        self.nums = []
        self.N = 0
        self.SUM = 0

    def addNum(self, num: int):
        self.nums.append(num)
        self.median = sum(self.nums)