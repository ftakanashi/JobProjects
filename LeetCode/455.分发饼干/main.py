#!/usr/bin/env python
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0: return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                j += 1
            i += 1
        return res