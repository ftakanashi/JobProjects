#!/usr/bin/env python

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        indices = []
        prev = None
        for i, ch in enumerate(s):
            if ch != prev:
                prev = ch
                indices.append(i)
        indices.append(len(s))
        if len(indices) < 3: return 0
        ans = 0
        for i in range(len(indices)-2):
            ans += min(indices[i+1] - indices[i], indices[i+2] - indices[i+1])
        return  ans