#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        opes = "&|!"
        for ch in expression:
            if ch == "t":
                stack.append(True)
            elif ch == "f":
                stack.append(False)
            elif ch in opes:
                stack.append(ch)
            elif ch == "(":
                pass
            elif ch == ")":
                bools = []
                while stack and type(stack[-1]) is bool:
                    bools.append(stack.pop())
                ope = stack.pop()
                if ope == "&":
                    stack.append(all(bools))
                elif ope == "|":
                    stack.append(any(bools))
                else:
                    stack.append(not bools[0])
        return stack[0]