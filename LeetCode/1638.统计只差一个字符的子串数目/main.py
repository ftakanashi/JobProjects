#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import lru_cache as cache

class Solution:

    @cache
    def check(self, span1: str, span2: str) -> bool:
        assert len(span1) == len(span2)
        diff = 0
        for i in range(len(span1)):
            if span1[i] == span2[i]: continue
            diff += 1
            if diff > 1: return False
        return diff == 1

    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m, n = len(s), len(t)
        for i in range(m):
            for j in range(n):

                for l in range(1, min(m - i, n - j) + 1):
                    if self.check(s[i:i + l], t[j:j + l]):
                        ans += 1
        return ans