#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_l, new_r = newInterval

        res = []
        intervals.append([float('inf'), float('inf')])    # dummy
        for i, (l, r) in enumerate(intervals):
            if not (r < new_l or l > new_r):
                # 有交集
                new_l, new_r = min(l, new_l), max(r, new_r)
            else:
                # 无交集
                if l > new_r:
                    # 当遍历到的区间完全在newInterval的右边
                    res.append([new_l, new_r])
                    break
                res.append([l, r])

        while i < len(intervals):    # 把没遍历到的右边所有区间再收割
            res.append(intervals[i])
            i += 1

        intervals.pop()    # 恢复intervals
        return res[:-1]    # 返回结果去掉dummy