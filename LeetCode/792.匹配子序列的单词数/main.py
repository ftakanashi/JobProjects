#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from functools import lru_cache as cache

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)

        @cache
        def check(word):
            i = j = 0
            m = len(word)
            while i < m and j < n:
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == m

        ans = 0
        for word in words:
            if check(word):
                ans += 1
        return ans