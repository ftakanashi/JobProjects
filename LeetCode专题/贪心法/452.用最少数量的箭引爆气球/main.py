#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arr = -1
        count = 0
        i = 0
        while i < len(points):
            arr = points[i][1]
            count += 1
            while i < len(points) and points[i][0] <= arr:
                # 跳过所有可以被这只箭戳爆的气球
                i += 1
        return count