#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import bisect
from functools import lru_cache as cache
from collections import Counter

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        @cache
        def f(s):
            min_ch = "{"
            cnt = Counter()
            for ch in s:
                if ch < min_ch:
                    min_ch = ch
                cnt[ch] += 1
            return cnt[min_ch]

        word_vals = [f(word) for word in words]
        word_vals.sort()
        ans = []
        for q in queries:
            q_val = f(q)
            ans.append(len(word_vals) - bisect.bisect(word_vals, q_val))
        return ans