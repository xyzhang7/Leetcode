from functools import lru_cache


def numDecodings(s: str) -> int:
    N = len(s)
    if N == 0 or s[0] == '0':
        return 0

    dp = [0] * (N+1)
    dp[N] = 1
    for i in range(N - 1, -1, -1):
        if s[i] == '0':
            if i == 0 or int(s[i-1:i+1]) > 26:
                return 0
            continue
        elif i < N-1 and int(s[i:i + 2]) <= 26:
            dp[i] += dp[i + 2]
        dp[i] += dp[i + 1]
    return dp[0]

def numDecodingsConstactSpace(s: str) -> int:
    """
    O(1) space
    """
    n = len(s)
    if s[0] == '0':
        return 0
    p, pp = 1, 0
    for i in range(n-2, -1, -1):
        cur = p
        if s[i] == '0' and int(s[i - 1:i + 1]) > 26:
            return 0
        if s[i] == '0':
            cur = 0
        elif i < n-1 and int(s[i:i+2]) <= 26:
            cur += pp
        p, pp = cur, p
    return p


def numDecodingsRecurMemo(s: str) -> str:
    """
    recur + memo (lru_cache)
    NOTE: In memo (lru_cache), the key is parsed function signature, value is return value)
          If we set @lru_cache(max_size=0), there is no cache,
          If we set @lru_cache(max_size=None), the size is unlimited,
          If we set @lru_cache, the one without argument, the size is set as default value 128
    """
    N = len(s)

    @lru_cache
    def recur(idx):
        if s[idx] == '0':
            return 0
        if idx == N-1 and int(s[idx]) <= 26:
            return 1
        if idx == N-2 and int(s[idx:idx+2]) <= 26:
            return 1+recur(idx+1)

        ans = recur(idx+1)
        if int(s[idx:idx+2]) <= 26:
            ans += recur(idx+2)
        return ans
    return recur(0)



if __name__ == "__main__":
    numDecodingsRecurMemo("160")