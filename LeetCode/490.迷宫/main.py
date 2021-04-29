#!/usr/bin/env python

from typing import List
from functools import lru_cache as cache

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for _ in range(n)] for _ in range(m)]

        @cache
        def dfs(x, y):
            if visited[x][y] == 1: return False
            visited[x][y] = 1
            for d0, d1 in direcs:
                nx, ny = x, y
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += d0
                    ny += d1
                nx -= d0
                ny -= d1
                if destination == [nx, ny] or dfs(nx, ny): return True

            return False

        return dfs(*start)