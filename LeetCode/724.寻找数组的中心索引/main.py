#!/usr/bin/env python
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        i = 0
        while i < len(nums):
            if total - 2 * s == nums[i]:
                return i
            s += nums[i]
            i += 1
        return -1