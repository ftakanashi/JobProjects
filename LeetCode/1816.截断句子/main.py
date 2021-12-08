#!/usr/bin/env python
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cnt = 0
        pos = len(s)
        for i, ch in enumerate(s):
            if ch == ' ':
                cnt += 1
                if cnt == k:
                    pos = i
                    break
        return s[:pos]