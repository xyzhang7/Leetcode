def isHappy(n: int) -> bool:
    prev = n
    while n != 1:
        curr = 0
        while n > 0:
            curr += (n % 10) ** 2
            n = n // 10

        if curr == prev:
            return False

        prev = n = curr

    return True

if __name__ == "__main__":
    isHappy(2)