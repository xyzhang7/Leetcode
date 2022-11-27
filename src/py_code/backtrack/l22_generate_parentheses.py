from typing import List


def generateParenthesis(n: int) -> List[str]:
    ans = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack("", 0, 0)
    return ans

if __name__ == '__main__':
    generateParenthesis(3)