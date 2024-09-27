#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = 0
        last = -1
        for x, y in points:
            if x > last:
                last = x + w
                ans += 1
        return ans