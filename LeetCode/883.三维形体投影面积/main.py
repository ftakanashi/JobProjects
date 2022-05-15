#!/usr/bin/env python
from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0
        n = len(grid)
        max_rows = [0 for _ in range(n)]
        max_cols = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0: top += 1
                max_rows[i] = max(max_rows[i], grid[i][j])
                max_cols[j] = max(max_cols[j], grid[i][j])

        return top + sum(max_rows) + sum(max_cols)