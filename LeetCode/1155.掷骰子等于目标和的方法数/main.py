#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(target + 1):
                for num in range(1, k + 1):
                    if j - num >= 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-num]) % MOD
        return dp[-1][-1]