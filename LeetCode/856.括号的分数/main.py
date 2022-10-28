#!/usr/bin/env python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif stack[-1] == "(":
                stack.pop()
                stack.append(1)
            else:
                score = 0
                while type(stack[-1]) is int:
                    score += stack.pop()
                stack.pop()
                stack.append(score * 2)
        return sum(stack)