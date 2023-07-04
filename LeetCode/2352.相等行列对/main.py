#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = Counter()
        for row in grid:
            counter[tuple(row)] += 1

        ans = 0
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            col = tuple(col)
            ans += counter[col]
        return ans