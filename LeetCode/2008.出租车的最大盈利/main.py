#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import defaultdict
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        tmp = defaultdict(list)
        for s, e, tips in rides:
            tmp[e].append((s, e - s + tips))

        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            maybe = 0
            for s, profit in tmp[i]:
                maybe = max(maybe, dp[s] + profit)

            dp[i] = max(dp[i - 1], maybe)

        return dp[-1]