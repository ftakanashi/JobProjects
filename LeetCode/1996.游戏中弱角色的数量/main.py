#!/usr/bin/env python
from typing import List

class Solution1:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0
        for p in properties:
            while stack and stack[-1][1] < p[1]:
                stack.pop()
                ans += 1
            stack.append(p)
        return ans

class Solution2:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        ans = 0
        max_def = -1
        for p in properties:
            if p[1] < max_def:
                ans += 1
            else:
                max_def = p[1]
        return ans