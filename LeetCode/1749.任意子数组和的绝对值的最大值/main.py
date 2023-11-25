#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = _min = _max = ans = 0
        for num in nums:
            s += num
            ans = max(ans, s - _min, _max - s)
            _min = min(_min, s)
            _max = max(_max, s)

        return ans