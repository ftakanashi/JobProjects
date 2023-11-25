#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = Counter(), Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                rows[i] += 1
                cols[j] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                if rows[i] > 1 or cols[j] > 1:
                    ans += 1
        return ans