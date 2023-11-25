#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()

        h_max = h_prev = 0
        v_max = v_prev = 0

        # 计算水平方向最大间距
        for _h in horizontalCuts:
            h_max = max(h_max, _h - h_prev)
            h_prev = _h
        h_max = max(h_max, h - horizontalCuts[-1])    # 别忘了最后一刀到末尾的距离

        # 计算垂直方向最大间距
        for v in verticalCuts:
            v_max = max(v_max, v - v_prev)
            v_prev = v
        v_max = max(v_max, w - verticalCuts[-1])    # 别忘了最后一刀到末尾的距离

        return (h_max % MOD) * (v_max % MOD) % MOD