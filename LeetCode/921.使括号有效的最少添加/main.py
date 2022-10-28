#!/usr/bin/env python

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = ans = 0
        for ch in s:
            if ch == "(":
                stack += 1
            elif stack:
                stack -= 1
            else:
                ans += 1

        ans += stack
        return ans