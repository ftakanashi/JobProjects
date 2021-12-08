#!/usr/bin/env python
from typing import List

DIRECS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def checkBorder(self, grid: List[List[int]], x: int, y: int) -> bool:
        m, n = len(grid), len(grid[0])
        for a, b in DIRECS:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != grid[x][y]:
                return True
        return False

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = grid[i][j]

        visited = set()
        def dfs(x, y):
            visited.add((x, y))
            res[x][y] = 0
            for a, b in DIRECS:
                nx, ny = x+a, y+b
                if (nx, ny) in visited: continue
                if nx < 0 or nx >= m or ny < 0 or ny >=n: continue
                if grid[nx][ny] != grid[x][y]: continue
                dfs(nx, ny)

        dfs(row, col)

        for i in range(m):
            for j in range(n):
                if res[i][j] == 0:
                    if self.checkBorder(grid, i, j):
                        res[i][j] = color
                    else:
                        res[i][j] = grid[i][j]
        return res