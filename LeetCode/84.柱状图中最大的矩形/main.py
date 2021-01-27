#!/usr/bin/env python
from typing import List

class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0: return 0
        l_bond, r_bond = [], []

        stack = []
        for i in range(n):
            h = heights[i]
            while len(stack) > 0 and h <= heights[stack[-1]]:
                stack.pop()
            l_bond.append(-1 if len(stack) == 0 else stack[-1])
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            h = heights[i]
            while len(stack) > 0 and h <= heights[stack[-1]]:
                stack.pop()
            r_bond.append(n if len(stack) == 0 else stack[-1])
            stack.append(i)
        r_bond.reverse()

        max_rec = 0
        for i in range(n):
            max_rec = max(max_rec, (r_bond[i] - l_bond[i] - 1) * heights[i])
        return max_rec

class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        if n == 0: return 0

        l_bond = [-1 for _ in range(n)]
        r_bond = [n for _ in range(n)]
        max_rec = 0
        stack = []
        for i in range(n):
            h = heights[i]
            while len(stack) > 0 and h <= heights[stack[-1]]:
                j = stack.pop()
                r_bond[j] = i    # 关键
            l_bond[i] = stack[-1] if len(stack) > 0 else -1
            stack.append(i)

        for i in range(n):
            max_rec = max(max_rec, heights[i] * (r_bond[i] - l_bond[i] - 1))
        return max_rec