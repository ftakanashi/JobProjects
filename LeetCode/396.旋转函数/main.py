#!/usr/bin/env python
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        ans = total = sum(i * nums[i] for i in range(n))
        s = sum(nums)

        for i in range(n-1, -1, -1):
            total = total - (n-1) * nums[i] + (s - nums[i])
            ans = max(ans, total)
        return ans