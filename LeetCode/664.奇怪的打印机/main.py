#!/usr/bin/env python
from typing import List

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1    # 初始化

        # 斜向遍历，以子串长度l作为线索进入遍历
        for l in range(1, n):
            i, j = 0, l    # 从对角线开始，逐渐向右上角一行一行地斜向前进
            while j < n:
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i,j))
                i += 1
                j += 1
        # print(dp)
        return dp[0][-1]