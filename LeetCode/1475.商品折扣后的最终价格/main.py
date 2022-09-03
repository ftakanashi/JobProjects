#!/usr/bin/env python
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        tmp = []
        n = len(prices)
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while stack and prices[stack[-1]] > p:
                stack.pop()

            tmp.append(stack[-1] if stack else n)
            stack.append(i)
        tmp.reverse()

        prices.append(0)
        return [p - prices[t] for p, t in zip(prices, tmp)]