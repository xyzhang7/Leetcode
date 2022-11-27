def solution(a, b, k):
    def digits(number):
        d = 0
        while number > 0:
            d += 1
            number //= 10
        return d
    result = 0
    for i in range(len(a)):
        if a[i] * (10 ** digits(b[i])) + b[i] < k:
            result += 1
    return result

if __name__ == "__main__":
    solution([1, 2, 3], [1, 2, 3], 32)