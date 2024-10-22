#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            ans = min(
                ans,
                max(nums[-1] - k, nums[i] + k) - min(nums[0] + k, nums[i+1] - k)
            )
        return ans