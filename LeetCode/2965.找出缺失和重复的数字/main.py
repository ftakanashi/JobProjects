#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        duplicate = lack = -1
        n = len(grid)
        i = 0
        while i < n ** 2:
            x, y = i // n, i % n

            # 只要当前位置不是预期值，就不断将其交换到其预期为止
            while i < n ** 2 and grid[x][y] is not None and grid[x][y] != (i + 1):
                tx, ty = (grid[x][y] - 1) // n, (grid[x][y] - 1) % n
                if grid[tx][ty] != grid[x][y]:
                    grid[tx][ty], grid[x][y] = grid[x][y], grid[tx][ty]
                else:
                    duplicate = grid[x][y]
                    grid[x][y] = None
                    break
            i += 1

        for i, j in [(i, j) for i in range(n) for j in range(n)]:
            if grid[i][j] is None:
                lack = (i * n) + j + 1
                return [duplicate, lack]