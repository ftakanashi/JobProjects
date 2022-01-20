#!/usr/bin/env python
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = x = 0
        for ch in s:
            if ch == '(':
                x += 1
                ans = max(ans, x)
            elif ch == ')':
                x -= 1
        return ans