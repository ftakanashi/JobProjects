#!/usr/bin/env python
from typing import List
from functools import lru_cache as cache

class Solution:
    def analyze(self, expression: str):
        digits = set("1234567890")
        items = []
        i = 0
        while i < len(expression):
            if expression[i] in digits:
                num = 0
                while i < len(expression) and expression[i] in digits:
                    num = num * 10 + int(expression[i])
                    i += 1
                items.append(num)
            else:
                items.append(expression[i])
                i += 1
        return items

    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        items = self.analyze(expression)
        n = len(items)
        assert type(items[0]) is int

        func_map = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: x - y,
            "*": lambda x,y: x * y
        }

        @cache
        def rec(start, end):
            if start == end: return [items[start], ]

            res = []
            for i in range(start, end + 1):
                if type(items[i]) is int: continue
                left = rec(start, i - 1)
                right = rec(i + 1, end)
                opt = items[i]
                for l in left:
                    for r in right:
                        res.append(func_map[opt](l, r))
            return res

        return rec(0, len(items) - 1)