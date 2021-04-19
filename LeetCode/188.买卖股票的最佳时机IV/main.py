#!/usr/bin/env python

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0: return 0
        dp = [float('-inf') for _ in range(k*2+1)]
        dp[0] = 0
        dp[1] = -prices[0]
        flag = [1, -1]
        for i in range(1, len(prices)):
            p = prices[i]
            for j in range(1, k*2+1):
                dp[j] = max(dp[j], dp[j-1] + flag[j&1] * p)

        return max(dp)