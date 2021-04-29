#!/usr/bin/env python

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [num for num in nums]
        dp_min = [num for num in nums]
        for i in range(1, n):
            cands = [nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i]]
            dp_max[i] = max(cands)
            dp_min[i] = min(cands)

        return max(dp_max)