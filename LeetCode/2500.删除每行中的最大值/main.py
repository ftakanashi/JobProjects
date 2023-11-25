#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)

        ans = 0
        for j in range(len(grid[0])):
            ans += max(grid[i][j] for i in range(len(grid)))
        return ans