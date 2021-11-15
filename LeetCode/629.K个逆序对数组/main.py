#!/usr/bin/env python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i][j-1] - (dp[i-1][j-i] if j >= i else 0) + dp[i-1][j]
                dp[i][j] = dp[i][j] % MOD
        return dp[-1][-1]