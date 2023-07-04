#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque()
        queue.append((0, 0, 1))
        seen = set()
        n = len(grid)
        direcs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        while queue:
            x, y, step = queue.popleft()
            if (x, y) in seen: continue
            if x == n - 1 and y == n - 1:
                return step
            seen.add((x, y))
            for a, b in direcs:
                nx, ny = x + a, y + b
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                # if (nx, ny) in seen: continue
                if grid[nx][ny] == 1: continue
                queue.append((nx, ny, step + 1))

        return -1