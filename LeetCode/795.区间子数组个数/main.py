#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def check(upper):
            res = cur = 0
            for num in nums:
                if num <= upper:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res

        return check(right) - check(left - 1)