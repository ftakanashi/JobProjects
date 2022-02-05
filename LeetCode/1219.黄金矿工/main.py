#!/usr/bin/env python
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direcs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x, y, gold):
            cur_gold = grid[x][y]
            max_gold = new_gold = cur_gold + gold
            grid[x][y] = 0
            for a, b in direcs:
                nx, ny = x+a, y+b
                if nx in (-1, m) or ny in (-1, n) or grid[nx][ny] == 0: continue
                max_gold = max(max_gold, dfs(nx, ny, new_gold))
            grid[x][y] = cur_gold    # 回溯
            return max_gold

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                ans = max(ans, dfs(i, j, 0))
        return ans