#!/usr/bin/env python
from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x == m: return y
            if grid[x][y] == 1:
                if y+1 == n or grid[x][y+1] == -1: return -1
                return dfs(x+1, y+1)
            else:
                if y == 0 or grid[x][y-1] == 1: return -1
                return dfs(x+1, y-1)

        ans = []
        for j in range(n):
            ans.append(dfs(0, j))
        return ans