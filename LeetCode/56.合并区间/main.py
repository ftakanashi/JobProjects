#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0 or len(intervals) == 1: return intervals

        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0], ]
        i = 1
        while i < len(intervals):
            x, y = intervals[i]
            a, b = merged[-1]
            if x > b:
                merged.append([x, y])
            else:
                a, b = min(a, x), max(b, y)
                merged[-1] = [a, b]
            i += 1
        return merged