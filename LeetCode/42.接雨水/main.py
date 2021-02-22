#!/usr/bin/env python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                base = height[stack.pop()]
                if not stack: break
                l_height, r_height = height[stack[-1]], height[i]
                res += (min(l_height, r_height) - base) * (i - stack[-1] - 1)
            stack.append(i)
        return res