#!/usr/bin/env python

from typing import List

import collections
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for n in c:
            if c[n] == 1: return n

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = sum(n >> i & 1 for n in nums)
            if count % 3 == 0: continue
            if i < 31:
                res = res | (1 << i)
            else:
                res -= 2**31
        return res