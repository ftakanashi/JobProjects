#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j, n = 1, 0, len(pushed)
        if n == 0 or n == 1: return True
        stack = [pushed[0],]

        while i < n:
            while i < n and (len(stack) == 0 or stack[-1] != popped[j]):
                stack.append(pushed[i])
                i += 1

            while j < n and len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return len(stack) == 0
