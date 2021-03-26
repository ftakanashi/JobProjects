#!/usr/bin/env python

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack, seen = [], set()

        for ch in s:
            if ch in seen:
                counter[ch] -= 1
                continue
            while stack and ch < stack[-1] and counter[stack[-1]] > 1:
                counter[stack[-1]] -= 1
                seen.remove(stack[-1])
                stack.pop()

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)