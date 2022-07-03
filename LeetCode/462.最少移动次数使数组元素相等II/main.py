#!/usr/bin/env python
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) & 1 == 1:
            std = nums[len(nums) // 2]
        else:
            std = nums[len(nums) // 2 - 1]

        return sum(abs(std - num) for num in nums)