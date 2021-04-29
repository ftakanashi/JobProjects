#!/usr/bin/env python

from typing import List
import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, start[0], start[1])]
        while heap:
            d, x, y = heapq.heappop(heap)
            if dist[x][y] <= d: continue
            dist[x][y] = d
            for d0, d1 in direcs:
                nx, ny, nd = x, y, d
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += d0
                    ny += d1
                    nd += 1
                nx -= d0
                ny -= d1
                nd -= 1
                if destination == [nx, ny]: return nd
                heapq.heappush(heap, (nd, nx, ny))

        return -1