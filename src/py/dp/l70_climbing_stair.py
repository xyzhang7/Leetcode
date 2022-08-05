def climbStairs(n: int) -> int:
    dp = [1] * 3

    for i in range(2, n + 1):
        dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]

    return dp[n % 3]

if __name__ == "__main__":
    print(climbStairs(2))
    # print(climbStairs(3))