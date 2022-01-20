#!/usr/bin/env python
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid-1]:
                if mid & 1 == 1:
                    l = mid + 1
                else:
                    r = mid - 2
            elif nums[mid] == nums[mid+1]:
                if mid & 1 == 1:
                    r = mid - 1
                else:
                    l = mid + 2
            else:
                return nums[mid]
        return nums[l]