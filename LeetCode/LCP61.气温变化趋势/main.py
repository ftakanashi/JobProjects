#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        n = len(temperatureA)
        ans = span = 0
        for i in range(1, n):
            a = temperatureA[i] - temperatureA[i-1]
            b = temperatureB[i] - temperatureB[i-1]
            if a == b == 0 or (a > 0 and b > 0) or (a < 0 and b < 0):
                span += 1
            else:
                span = 0
            ans = max(ans, span)
        return ans