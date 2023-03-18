#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        queue = profit = max_profit = ans = times = 0

        for num in customers:
            queue += num
            times += 1
            profit += (min(4, queue) * boardingCost - runningCost)
            queue = max(queue - 4, 0)
            if profit > max_profit:
                ans = times
                max_profit = profit

        while queue > 0:
            times += 1
            profit += (min(4, queue) * boardingCost - runningCost)
            queue = max(queue - 4, 0)
            if profit > max_profit:
                ans = times
                max_profit = profit

        return ans if ans > 0 else -1