import collections
import heapq


def minDeletions(s: str) -> int:
    chars_count = collections.Counter(s)
    frequency = sorted(chars_count.values())
    frequency = [-1 * i for i in frequency]
    heapq.heapify(frequency)
    delete_count = 0
    while frequency:
        top = heapq.heappop(frequency)
        if frequency and top == frequency[0]:
            top += 1
            delete_count += 1
            heapq.heappush(frequency, top)
    return delete_count


if __name__ == '__main__':
    minDeletions("bbcebab")