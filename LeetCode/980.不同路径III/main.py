#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        total = 0
        sx = sy = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] in (0, 1):
                    total += 1
                    if grid[i][j] == 1:
                        sx, sy = i, j

        def dfs(x, y, rest):
            if grid[x][y] == 2:
                return 0 if rest > 0 else 1
            res = 0
            tmp = grid[x][y]
            grid[x][y] = -1
            for a, b in direcs:
                nx, ny = x + a, y + b
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if grid[nx][ny] not in (0, 2): continue
                res += dfs(nx, ny, rest - 1)
            grid[x][y] = tmp
            return res

        return dfs(sx, sy, total)