#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                queue.append((i, j, 0))

        visited = set()
        ans = -1
        while queue:
            x, y, times = queue.popleft()
            if (x, y) in visited: continue
            visited.add((x, y))
            ans = max(ans, times)
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = x+d[0], y+d[1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    queue.append((nx, ny, times + 1))
        return ans if ans > 0 else -1