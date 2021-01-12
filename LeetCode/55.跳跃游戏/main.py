#!/usr/bin/env python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        max_pos = nums[0]
        while i <= max_pos and i < n:
            max_pos = max(i + nums[i], max_pos)
            if max_pos >= n - 1:
                return True
            i += 1

        return False