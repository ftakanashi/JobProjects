#!/usr/bin/env python
from typing import List

from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        queue = deque()
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))

        direcs = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            x, y, h = queue.popleft()
            for a, b in direcs:
                nx, ny = x+a, y+b
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if isWater[nx][ny] == 1: continue
                if ans[nx][ny] == 0:
                    ans[nx][ny] = h + 1
                    queue.append((nx, ny, h+1))
        return ans