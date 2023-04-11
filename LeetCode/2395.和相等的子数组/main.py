#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            mid = (nums[i] + nums[i + 1]) / 2
            if int(mid) == mid:
                sign = (int(mid), True)
            else:
                sign = (int(mid), False)
            if sign in seen: return True
            seen.add(sign)
        return False