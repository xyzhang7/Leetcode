def solution(grid, shots):
    ans = []
    n, m = len(grid), len(grid[0])
    attacked = []
    for r in grid:
        attacked.append(grid[r][:])
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    sunk = set()

    def dfs(x, y, ship):
        x1, y1 = x - 1, y - 1
        x2, y2 = x + 1, y + 1
        while 0 <= x1 and grid[x1][y] == ship:
            if attacked[x1][y] == ship:
                return False
            elif attacked[x1][y] == '0':
                x1 -= 1
        while n > x2 and grid[x2][y] == ship:
            if attacked[x2][y] == ship:
                return False
            elif attacked[x2][y] == '0':
                x2 += 1
        while 0 <= y1 and grid[x][y1] == ship:
            if attacked[x][y1] == ship:
                return False
            elif attacked[x][y1] == '0':
                y1 -= 1
        while m > y2 and grid[x][y2] == ship:
            if attacked[x][y2] == ship:
                return False
            elif attacked[x][y2] == '0':
                y2 += 1
        return True

    for s in shots:
        if grid[s[0]][s[1]] == '.':
            ans.append("Missed")
            continue
        ship = grid[s[0]][s[1]]
        attack = attacked[s[0]][s[1]]
        if attack == '0':
            ans.append("Already attacked")
            continue
        if ship in sunk:
            ans.append(f"Ship {ship} sunk")
            continue

        if attack != '0':
            attacked[s[0]][s[1]] = '0'
        is_sunk = dfs(s[0], s[1], ship)
        if is_sunk:
            ans.append(f"Ship {ship} sunk")
            sunk.add(ship)
        else:
            ans.append(f"Attacked ship {ship}")
    return ans


if __name__ == '__main__':
    grid =   [["6","6","6"],
             ["4","7","7"],
             ["3","3","1"]]
    shots = [[2,1],
 [1,2],
 [1,1],
 [1,1],
 [2,0],
 [2,0],
 [2,2],
 [2,0],
 [0,1],
 [0,2],
 [2,2],
 [2,2],
 [1,0],
 [1,2],
 [0,2],
 [2,0],
 [0,0],
 [0,2]]
    solution(grid, shots)