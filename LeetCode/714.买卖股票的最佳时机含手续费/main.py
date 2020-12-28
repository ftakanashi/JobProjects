#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # 非状态压缩版代码
        # dp = [[0, 0] for _ in range(n)]
        # dp[0][1] = -prices[0]
        # for i in range(1, n):
        #     price = prices[i]
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price - fee)
        #     dp[i][1] = max(dp[i-1][0] - price, dp[i-1][1])
        # return max(dp[-1])

        sell_prof, hold_prof = 0, -prices[0]
        for i in range(1, n):
            sell_prof = max(sell_prof, hold_prof + prices[i] - fee)
            hold_prof = max(sell_prof - prices[i], hold_prof)

        return max(sell_prof, hold_prof)