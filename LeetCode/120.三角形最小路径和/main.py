#!/usr/bin/env python
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf') for _ in range(n)]
        dp[0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] += triangle[i][0]
        return min(dp)