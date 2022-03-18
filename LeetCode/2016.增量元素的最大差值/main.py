#!/usr/bin/env python

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            ans = max(stack[-1] - stack[0], ans)
        return -1 if ans == 0 else ans