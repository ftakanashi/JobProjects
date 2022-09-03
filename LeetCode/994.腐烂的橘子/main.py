#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        ans = 0
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue and fresh > 0:
            ans += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for a, b in direcs:
                    nx, ny = x + a, y + b
                    if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1

        return ans if fresh == 0 else -1