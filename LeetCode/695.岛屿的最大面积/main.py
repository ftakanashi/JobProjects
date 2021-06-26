#!/usr/bin/env python

from typing import List
from collections import deque

class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i,j) in seen: continue

                queue = deque()
                queue.append((i, j))
                area = 0
                while queue:
                    x, y = queue.popleft()
                    if (x, y) in seen: continue
                    seen.add((x, y))
                    area += 1
                    for a, b in direcs:
                        nx, ny = x+a, y+b
                        if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in seen or grid[nx][ny] == 0: continue
                        queue.append((nx, ny))

                res = max(res, area)

        return res

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            visited.add((x, y))
            area = 1
            for a, b in direcs:
                na, nb = x + a, y + b
                if na < 0 or na >= m or nb < 0 or nb >= n or (na, nb) in visited or grid[na][nb] == 0: continue
                area += dfs(x+a, y+b)
            return area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, dfs(i, j))
        return res