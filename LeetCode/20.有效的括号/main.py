#!/usr/bin/env python

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bmap = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch not in bmap:    # left
                stack.append(ch)
            else:
                if len(stack) == 0: return False
                pa = stack.pop()
                if bmap[ch] != pa: return False

        return len(stack) == 0