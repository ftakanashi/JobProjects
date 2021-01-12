#!/usr/bin/env python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[0] + grid[i][0]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]

        return dp[-1]