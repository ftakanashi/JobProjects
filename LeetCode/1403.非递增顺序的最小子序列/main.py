#!/usr/bin/env python
from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        s = sum(nums)
        curr = 0
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            curr += nums[i]
            ans.append(nums[i])
            if curr > s // 2:
                break

        return ans