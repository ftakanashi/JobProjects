#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        mod = 10**9 + 7
        dp = [[0, 0, 0, 0] for _ in range(n)]
        dp[0] = [1, 0, 0, 1]
        for i in range(1, n):
            dp[i][0] = dp[i-1][3] % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod
            dp[i][3] = sum(dp[i-1]) % mod

        return dp[-1][3]