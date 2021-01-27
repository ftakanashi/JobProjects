#!/usr/bin/env python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                a = stack.pop()
                b = stack.pop()
                if token == '+': res = a + b
                elif token == '-': res = b - a
                elif token == '*': res = a * b
                else: res = int(b / a)
                stack.append(res)
            else:
                n = int(token)
                stack.append(n)
        return stack[0]