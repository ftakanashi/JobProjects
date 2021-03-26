#!/usr/bin/env python
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums * 2
        stack = []
        res = []
        for i in range(2*n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if i < n:
                res.append(nums[stack[-1]] if stack else -1)
            stack.append(i)
        res.reverse()

        return res