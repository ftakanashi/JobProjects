#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                queue.append(grid[i][j])

        k = k % (m * n)
        for _ in range(k):
            queue.appendleft(queue.pop())

        for i in range(m):
            for j in range(n):
                grid[i][j] = queue.popleft()
        return grid