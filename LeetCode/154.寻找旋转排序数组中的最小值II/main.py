#!/usr/bin/env python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
            else:
                r -= 1

        return min(nums[l], nums[r])