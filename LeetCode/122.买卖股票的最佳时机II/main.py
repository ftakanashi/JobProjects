#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            p = prices[i + 1] - prices[i]
            if p > 0:
                res += p
        return res

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]

        dp[0][1] = -prices[0]
        for i in range(1, n):
            price = prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price)
            dp[i][1] = max(dp[i-1][0] - price, dp[i-1][1])

        return max(dp[-1])

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        sell_prof, hold_prof = 0, -prices[0]
        for i in range(1, n):
            price = prices[i]
            sell_prof = max(sell_prof, hold_prof + price)
            hold_prof = max(sell_prof - price, hold_prof)

        return max(sell_prof, hold_prof)