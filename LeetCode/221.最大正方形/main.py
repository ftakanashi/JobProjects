#!/usr/bin/env python
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 1:
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans ** 2