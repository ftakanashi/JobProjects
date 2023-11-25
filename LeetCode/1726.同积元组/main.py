#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter([nums[i] * nums[j] for i in range(n) for j in range(i + 1, n)])
        ans = 0
        for _, c in cnt.items():
            if c > 0:
                ans += (c * (c - 1) // 2 * 8)
        return ans