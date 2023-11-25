#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        MOD = 10 ** 9 + 7

        dp = [
            [[0 for _ in range(n)] for _ in range(m)]
            for _ in range(k + 1)
        ]

        apples = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] = apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
                apples[i][j] += (1 if pizza[i][j] == 'A' else 0)
                dp[1][i][j] = 1 if apples[i][j] > 0 else 0

        for k in range(1, k + 1):
            for i in range(m):
                for j in range(n):

                    for i2 in range(i + 1, m):
                        if apples[i][j] == apples[i2][j]: continue
                        dp[k][i][j] += dp[k - 1][i2][j]
                        dp[k][i][j] %= MOD

                    for j2 in range(j + 1, n):
                        if apples[i][j] == apples[i][j2]: continue
                        dp[k][i][j] += dp[k - 1][i][j2]
                        dp[k][i][j] %= MOD

        return dp[k][0][0]