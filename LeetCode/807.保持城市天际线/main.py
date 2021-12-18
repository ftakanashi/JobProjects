#!/usr/bin/env python
from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_row_height = [0 for _ in range(m)]
        max_col_height = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                h = grid[i][j]
                max_row_height[i] = max(max_row_height[i], h)
                max_col_height[j] = max(max_col_height[j], h)

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += (min(max_row_height[i], max_col_height[j]) - grid[i][j])
        return ans