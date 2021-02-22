#!/usr/bin/env python
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for n in arr:
            if not stack or n >= stack[-1]:
                stack.append(n)
            else:
                bound = stack.pop()
                while stack and n < stack[-1]:
                    stack.pop()
                stack.append(bound)
        return len(stack)