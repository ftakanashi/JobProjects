#!/usr/bin/env python
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == k:
            return nums[-1] - nums[0]
        ans = float('inf')
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i+k-1] - nums[i])
        return ans