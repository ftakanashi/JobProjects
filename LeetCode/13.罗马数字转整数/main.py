#!/usr/bin/env python

class Solution:
    def romanToInt(self, s: str) -> int:
        s2n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = []
        for c in s:
            n = s2n[c]
            if not stack or n <= stack[-1]:
                stack.append(n)
            else:
                stack.append(n - stack.pop())
        return sum(stack)