#!/usr/bin/env python
from typing import List

class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i - 1 < 0:
                left = -float('inf')
            else:
                left = nums[i - 1]

            if i + 1 >= len(nums):
                right = -float('inf')
            else:
                right = nums[i + 1]

            if nums[i] > left and nums[i] > right:
                return i

class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if mid - 1 < 0 or nums[mid - 1] < nums[mid]:
                l = mid
            else:
                r = mid

        return l if nums[l] > nums[r] else r