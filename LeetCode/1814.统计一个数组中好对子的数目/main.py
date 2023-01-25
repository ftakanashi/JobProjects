#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        contrib = Counter()
        for num in nums:
            tmp = num
            res = 0
            while tmp > 0:
                res = res * 10 + tmp % 10
                tmp = tmp // 10
            contrib[res - num] += 1

        ans = 0
        for val, cnt in contrib.items():
            ans += (cnt - 1) * cnt // 2
            ans = ans % MOD
        return ans