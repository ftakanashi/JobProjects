#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        total_land_edge = sum([sum(l) for l in grid]) * 4
        internal_edge = 0

        X, Y = len(grid), len(grid[0])
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        for x in range(X):
            for y in range(Y):
                for a, b in direc:
                    if 0<= x+a < X and 0 <= y+b < Y and \
                            grid[x][y] == 1 and grid[x+a][y+b] == 1:
                        internal_edge += 1

        return total_land_edge - internal_edge

class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    count += self.dfs(grid, x, y)    # 本题因为默认只有一个岛，所以其实也可以从任意一个陆地出发开始DFS。这里写成
                    # += 的话相当于可以针对"群岛"做统计

        return count

    def dfs(self, grid: List[List[int]], x: int, y: int) -> int:
        if grid[x][y] != 1:
            return 0
        else:
            grid[x][y] = 2    # 设置为2表示本块陆地已经遍历过了

        count = 0
        direc = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]

        for a, b in direc:
            if x + a < 0 or x + a >= len(grid) or y + b < 0 or y + b >= len(grid[0]) \
                    or grid[x+a][y+b] == 0:
                count += 1

            elif grid[x+a][y+b] == 1:
                count += self.dfs(grid, x + a, y + b)

            # else: pass  即 == 2的时候，直接pass掉

        return count