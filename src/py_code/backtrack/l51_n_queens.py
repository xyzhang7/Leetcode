from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    occupied_col = set()
    occupied_diag = set()
    occupied_anti = set()
    ans = []

    def get_row(c):
        cur_row = ""
        for i in range(n):
            if i == c:
                cur_row += "Q"
            else:
                cur_row += "."
        return cur_row

    def dfs(r, c, path):
        if not (c not in occupied_col and r - c not in occupied_diag and r + c not in occupied_anti):
            return
        path.append(get_row(c))
        occupied_col.add(c)
        occupied_diag.add(r - c)
        occupied_anti.add(r + c)
        if r == n-1:
            ans.append(path[:])
        for j in range(n):
            dfs(r + 1, j, path)
        occupied_col.remove(c)
        occupied_diag.remove(r-c)
        occupied_anti.remove(r+c)
        path.pop()

    for c in range(n):
        occupied_col = set()
        occupied_diag = set()
        occupied_anti = set()
        dfs(0, c, [])
    return ans

if __name__ == '__main__':
    solveNQueens(5)