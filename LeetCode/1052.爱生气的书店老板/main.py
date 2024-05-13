#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 计算前缀和
        n = len(customers)
        p1, p2 = [0, ], [0, ]
        for i in range(n):
            p1.append(p1[-1] + customers[i])
            p2.append(p2[-1] + customers[i] * (grumpy[i] ^ 1))

        ans = -1
        for i in range(n - minutes + 1):
            j = i + minutes - 1    # 计算窗口 (i, j)，注意窗口下表和前缀和下表不对等
            span_left = p2[i] - p2[0]
            span_right = p2[-1] - p2[j + 1]
            span = p1[j + 1] - p1[i]
            ans = max(ans, span_left + span + span_right)
        return ans