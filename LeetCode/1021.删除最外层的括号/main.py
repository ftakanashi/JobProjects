#!/usr/bin/env python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        stack = []
        prev = 0
        for i, ch in enumerate(s):
            if not stack or ch == "(":
                stack.append(ch)
            else:
                stack.pop()

            if len(stack) == 0:
                ans += s[prev + 1: i]
                prev = i + 1
        return ans