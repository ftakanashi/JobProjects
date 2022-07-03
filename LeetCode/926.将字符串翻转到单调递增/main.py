#!/usr/bin/env python

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0,0] for _ in range(n+1)]
        for i in range(1, n+1):
            if s[i-1] == "0":
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1])
        return min(dp[-1])