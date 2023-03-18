#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        tmp = 0
        for i in range(m):
            tmp += grid[i][0]
            dp[i][0] = tmp

        tmp = 0
        for j in range(n):
            tmp += grid[0][j]
            dp[0][j] = tmp

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]