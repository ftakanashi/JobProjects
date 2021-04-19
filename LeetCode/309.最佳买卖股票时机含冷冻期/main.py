#!/usr/bin/env python

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        dp = [[0, float('-inf'), float('-inf')] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        dp[1][2] = dp[0][1] + prices[1]
        for i in range(2, len(prices)):
            p = prices[i]
            dp[i][1] = max(dp[i-1][0] - p, dp[i-2][2] - p, dp[i-1][1])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + p)

        return max(dp[-1][-1], 0)