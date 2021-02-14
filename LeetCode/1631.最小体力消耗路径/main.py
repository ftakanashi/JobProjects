#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        visited = set([])
        queue = [(0, 0, 0)]
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [0] + [float('inf')] * (m * n - 1)
        while len(queue) > 0:
            cost, x, y = heapq.heappop(queue)
            if (x, y) in visited: continue
            visited.add((x, y))
            if x == m - 1 and y == n - 1: break
            for a, b in direcs:
                if 0 <= x + a < m and 0 <= y + b < n and max(cost, abs(heights[x+a][y+b]-heights[x][y])) <= dist[(x+a)*n+y+b]:
                    dist[(x+a)*n + y+b] = max(cost, abs(heights[x+a][y+b]-heights[x][y]))
                    heapq.heappush(queue, (dist[(x+a)*n + y+b], x+a, y+b))

        return dist[m*n-1]