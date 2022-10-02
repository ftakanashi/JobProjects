#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        while i <= nums[-1]:
            p = bisect.bisect_left(nums, i)
            if n - p == i:
                return i
            i += 1
        return -1