#!/usr/bin/env python
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        F = float('inf')
        dp = [[F for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1: continue
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)

        return dp[0][0]