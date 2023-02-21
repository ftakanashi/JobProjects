#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 填充DP数组
        dp = [[[0, 0] if grid[i][j] == 0 else [1, 1] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                if i > 0 and grid[i - 1][j] == 1:
                    dp[i][j][0] = dp[i - 1][j][0] + 1
                if j > 0 and grid[i][j - 1] == 1:
                    dp[i][j][1] = dp[i][j - 1][1] + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                for edge in range(min(dp[i][j]) - 1, -1, -1):
                    # 注意，这里的edge是README中提到的L，即尝试检查的正方形的边长再减去1
                    if dp[i - edge][j][1] >= edge + 1 and dp[i][j - edge][0] >= edge + 1:
                        ans = max(ans, edge + 1)
                        break

        return ans ** 2