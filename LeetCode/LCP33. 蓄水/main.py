#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        ans = float("inf")
        if max(vat) == 0: return 0
        for k in range(1, max(vat) + 1):
            tmp = 0
            for i in range(n):
                tmp += max(0, ceil(vat[i] / k) - bucket[i])
            ans = min(ans, tmp + k)
        return ans