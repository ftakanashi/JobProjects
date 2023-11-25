#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(t):
            cnt, prev = 0, False
            for num in nums:
                if num <= t and not prev:
                    prev = True
                    cnt += 1
                else:
                    prev = False
            return cnt >= k

        l, r = min(nums), max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l