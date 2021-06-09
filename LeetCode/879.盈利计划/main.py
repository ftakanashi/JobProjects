#!/usr/bin/env python
from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7

        m = len(profit)
        dp = [[[0] * (minProfit + 1) for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0][0] = 1

        for i in range(1, m+1):
            for j in range(n+1):
                for k in range(minProfit+1):
                    if j - group[i-1] >= 0:
                        dp[i][j][k] = (dp[i-1][j][k] +
                                       dp[i-1][j-group[i-1]][max(0, k-profit[i-1])]) % MOD
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

        res = sum(dp[-1][j][-1] for j in range(n+1)) % MOD
        return res