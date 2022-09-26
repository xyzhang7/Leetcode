from typing import List

def floodFill_DFS(image: List[List[int]], sr: int, sc:int, color: int) -> List[List[int]]:
    R, C = len(image), len(image[0])
    prev_color = image[sr][sc]
    if prev_color == color:
        return image
    def dfs(r, c):
        if image[r][c] == prev_color:
            image[r][c] = color
            if r >= 1: dfs(r-1, c)
            if r < R-1: dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c < C-1: dfs(r, c+1)
    dfs(sr, sc)
    return image