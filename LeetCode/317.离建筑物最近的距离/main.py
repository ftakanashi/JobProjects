#!/usr/bin/env python
from typing import List

from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0 for _ in range(n)] for _ in range(m)]    # 距离和矩阵
        build_count = [[0 for _ in range(n)] for _ in range(m)]    # 可达建筑物计数矩阵

        def bfs(x0, y0):
            visited = set()
            queue = deque()
            queue.append((x0, y0, 0))
            while queue:
                x, y, d = queue.popleft()
                if (x, y) in visited: continue
                visited.add((x, y))
                dist[x][y] += d
                build_count[x][y] += 1
                for a, b in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nx, ny = x+a, y+b
                    if nx < 0 or ny < 0 or nx == m or ny == n: continue
                    if grid[nx][ny] != 0: continue
                    queue.append((nx, ny, d+1))

        buildings = 0    # 顺便统计总共有几个建筑物
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    bfs(i, j)

        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and build_count[i][j] == buildings:
                    ans = min(ans, dist[i][j])
        return ans if ans < float('inf') else -1