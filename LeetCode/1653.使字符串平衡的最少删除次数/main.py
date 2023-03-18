#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt = Counter(s)
        ans = min(cnt["a"], cnt["b"])
        l, r = 0, cnt["a"]
        for ch in s:
            if ch == "b":
                l += 1
            else:
                r -= 1
            ans = min(ans, l + r)
        return ans