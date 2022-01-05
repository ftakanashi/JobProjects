#!/usr/bin/env python
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        flags = [[0 for _ in range(n)] for _ in range(m)]

        direcs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x, y, flag, seen):
            flags[x][y] |= flag
            seen.add((x, y))
            for a, b in direcs:
                nx, ny = x+a, y+b
                if nx < 0 or nx >= m or ny < 0 or ny >= n or \
                        (nx, ny) in seen or heights[nx][ny] < heights[x][y] or \
                        flags[nx][ny] & flag > 0:
                    # 只有下标合法 且 为在本次探索中探索过（防止循环）且 水流的逆向 且 明确知道那个位置还没有被标记过
                    # 才进行深入dfs
                    continue
                dfs(nx, ny, flag, seen)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(i, j, 1, set())
                if i == m-1 or j == n-1:
                    dfs(i, j, 2, set())

        ans = []
        for i in range(m):
            for j in range(n):
                if flags[i][j] == 3:
                    ans.append([i, j])
        return ans