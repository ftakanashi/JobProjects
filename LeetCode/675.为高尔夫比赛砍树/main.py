#!/usr/bin/env python
from typing import List

from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(start, end):
            sx, sy = start
            ex, ey = end
            queue = deque([(0, sx, sy)])
            seen = set()
            while queue:
                dist, x, y = queue.popleft()
                if (x, y) in seen: continue
                seen.add((x, y))
                if x == ex and y == ey:
                    return dist
                for a, b in direcs:
                    nx, ny = x + a, y + b
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and forest[nx][ny] > 0:
                        queue.append((dist + 1, nx, ny))
            return -1

        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1: trees.append((forest[i][j], i, j))
        trees.sort()    # 让所有树按照高度顺序从小到大排列好

        ans = 0
        prev = (0, 0)
        for _, i, j in trees:
            curr = (i, j)
            dist = bfs(prev, curr)
            if dist == -1: return -1
            ans += dist
            prev = curr
        return ans