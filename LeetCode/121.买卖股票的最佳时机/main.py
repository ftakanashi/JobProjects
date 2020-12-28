#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # 注意这两句不能反
            # 一定是先计算可能得到的最大利润，再把今天的售价维护成对未来而言的历史最低价
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit