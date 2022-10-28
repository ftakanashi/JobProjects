#!/usr/bin/env python
from typing import List
from collections import deque

class Solution1:
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


class Solution2:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def _find_one():
            i = 0
            while i < m:
                j = 0
                while j < n:
                    if grid[i][j] == 1:
                        grid[i][j] = -1
                        return i, j
                    j += 1
                i += 1

        i, j = _find_one()

        queue = deque([(i, j)])
        first = deque()
        while queue:
            x, y = queue.popleft()
            first.append((x, y))
            for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    queue.append((nx, ny))
                    grid[nx][ny] = -1

        ans = 0
        while first:
            for _ in range(len(first)):
                x, y = first.popleft()
                for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return ans
                        elif grid[nx][ny] == 0:
                            grid[nx][ny] = -1
                            first.append((nx, ny))
            ans += 1