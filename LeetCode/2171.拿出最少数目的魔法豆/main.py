#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        presum = [0]
        for b in beans:
            presum.append(presum[-1] + b)

        ans = float("inf")
        n = len(beans)
        for i in range(1, n + 1):
            tmp = presum[i - 1]
            tmp += presum[n] - presum[i] - (n - i) * beans[i - 1]
            ans = min(ans, tmp)
        return ans