#!/usr/bin/env python
from typing import List

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[[0,0,0,0] for j in range(n+2)] for i in range(m+2)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if mat[i-1][j-1] == 0: continue
                tmp = dp[i][j]
                tmp[0] = dp[i][j-1][0] + 1
                tmp[1] = dp[i-1][j][1] + 1
                tmp[2] = dp[i-1][j-1][2] + 1
                tmp[3] = dp[i-1][j+1][3] + 1
                ans = max(ans, max(tmp))
        return ans
