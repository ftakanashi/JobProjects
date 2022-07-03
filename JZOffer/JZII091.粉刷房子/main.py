#!/usr/bin/env python
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        rest = {
            0: (1, 2),
            1: (0, 2),
            2: (0, 1)
        }
        dp = costs[0].copy()
        for i in range(1, n):
            new = [0, 0, 0]
            for j in range(3):
                new[j] = costs[i][j] + min(dp[k] for k in rest[j])
            dp = new

        return min(dp)