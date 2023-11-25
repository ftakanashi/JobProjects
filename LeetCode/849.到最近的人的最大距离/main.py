#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n, i = len(seats), 0

        # 先获取到第一个1的位置
        while i < n and seats[i] == 0:
            i += 1
        ans = pre = i

        # 从第一个1的位置开始扫描
        while i < n:
            if seats[i] == 1:
                ans = max(ans, (i - pre) // 2)
                pre = i
            i += 1

        # 还需要考虑最后一个1以及其右边位置的可能性，此时pre就是最后一个1的位置
        ans = max(ans, len(seats) - 1 - pre)

        return ans