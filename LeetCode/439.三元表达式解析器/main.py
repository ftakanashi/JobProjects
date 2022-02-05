#!/usr/bin/env python

class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        expression = list(expression)
        while expression:
            ch = expression.pop()
            if ch == ":": continue
            elif ch == "?":
                flag = expression.pop()
                res = stack[-1] if flag == "T" else stack[-2]
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(ch)
        return stack[0]