#!/usr/bin/env python
from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        water = [[0 for _ in range(n)] for _ in range(m)]
        seen = set()
        heap = []

        # 先将边界的位置都入堆
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    water[i][j] = heightMap[i][j]
                    heapq.heappush(heap, (water[i][j], i, j))
                    seen.add((i, j))

        direcs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while heap:
            h, x, y = heapq.heappop(heap)
            # 探索堆顶位置周边位置
            for a, b in direcs:
                nx, ny = x+a, y+b
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in seen: continue
                water[nx][ny] = max(heightMap[nx][ny], h)    # 如果heightMap[nx][ny]更大，则说明不积水，换言之water[nx][ny] = heightMap[nx][ny]
                heapq.heappush(heap, (water[nx][ny], nx, ny))
                seen.add((nx, ny))

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += (water[i][j] - heightMap[i][j])
        return ans