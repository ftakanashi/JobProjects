#!/usr/bin/env python
from typing import List

class Solution:
    def getSpan(self, left: int, right: int) -> str:
        if left == right:
            return str(left)
        elif left < right:
            return f"{left}->{right}"
        return ''

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums: return [self.getSpan(lower, upper), ]
        i, p = lower, 0
        if nums[-1] < upper:
            nums.append(upper + 1)
        n = len(nums)
        ans = []
        while p < n:
            if i < nums[p]:
                ans.append(self.getSpan(i, nums[p] - 1))
            i = nums[p] + 1
            p += 1
        return ans