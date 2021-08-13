#!/usr/bin/env python

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf') for _ in range(5)] for _ in range(len(prices))]
        for i in range(len(prices)): dp[i][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - p)
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + p)
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - p)
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + p)
        return max(dp[-1])