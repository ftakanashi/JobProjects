#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from functools import lru_cache as cache

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        words_set = set(words)

        @cache
        def dfs(s):
            if s not in words_set:
                return 0
            else:
                ans = 0
                for i in range(len(s)):
                    ans = max(ans, dfs(s[:i] + s[i + 1:]))
                return ans + 1

        res = 0
        for word in words:
            res = max(res, dfs(word))
        return res