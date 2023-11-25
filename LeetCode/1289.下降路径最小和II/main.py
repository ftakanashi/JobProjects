#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        dp[0] = grid[0].copy()    # DP初始值，第一行和grid第一行一致

        # 求出第一行的最小值和次小值，以及各自对应坐标
        _min = _min2 = (-1, float("inf"))
        for j in range(n):
            if grid[0][j] < _min[1]:
                _min, _min2 = (j, grid[0][j]), _min
            elif grid[0][j] < _min2[1]:
                _min2 = (j, grid[0][j])

        # 开始DP
        for i in range(1, m):
            # 维护本行的最小值和次小值和对应下标
            n_min = n_min2 = (-1, float("inf"))

            for j in range(n):
                dp[i][j] = dp[i - 1][_min[0] if j != _min[0] else _min2[0]] + grid[i][j]

                if dp[i][j] < n_min[1]:
                    n_min2, n_min = n_min, (j, dp[i][j])
                elif dp[i][j] < n_min2[1]:
                    n_min2 = (j, dp[i][j])

            _min, _min2 = n_min, n_min2

        return min(dp[-1])