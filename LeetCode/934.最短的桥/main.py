#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        direc = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = set()
        def dfs(x, y):
            if x < 0 or y < 0 or x>=m or y>=n: return
            if (x, y) in seen: return
            if grid[x][y] == 0: return
            grid[x][y] = 2    # 将第一个岛的1标记为2
            seen.add((x, y))
            for a, b in direc:
                nx, ny = x+a, y+b
                dfs(nx, ny)

        m, n = len(grid), len(grid[0])
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = True    # 注意，只需要碰到第一个1后进行一次dfs即可
                    break
            if flag: break

        # 开始BFS
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:    # 从第二个岛的所有点出发遍历。这里改成2也没什么关系
                    queue.append((i, j, 0))

        seen = set()
        while queue:
            x, y, dist = queue.popleft()
            if grid[x][y] == 2: return dist - 1    # 题目问的是修改0的个数，而不是移动次数，所以要-1
            if (x, y) in seen: continue
            seen.add((x, y))

            for a, b in direc:
                nx = x + a
                ny = y + b
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                queue.append((nx, ny, dist + 1))
        return -1