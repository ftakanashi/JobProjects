#!/usr/bin/env python

from typing import List

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [1, ]
        for i in range(1, steps+1):
            if len(dp) < arrLen: dp.append(0)
            new_dp = dp.copy()

            for j in range(len(dp)):
                new_dp[j] += dp[j-1] if j > 0 else 0
                new_dp[j] += dp[j+1] if j < len(dp)-1 else 0
                if new_dp[j] > 10**9+7: new_dp[j] %= 10**9+7

            dp = new_dp

        return dp[0]