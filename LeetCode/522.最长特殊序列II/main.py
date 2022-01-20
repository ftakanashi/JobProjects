#!/usr/bin/env python
from typing import List

from collections import Counter
from functools import lru_cache as cache

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        counter = Counter(strs)
        keys = list(counter.keys())
        keys.sort(key=lambda x: len(x), reverse=True)

        @cache
        def isSub(sa, sb):    # 判断sa中是否包含一个子序列恰好是sb，保证sa.length >= sb.length
            if sa == sb: return True
            i = j = 0
            while i < len(sa) and j < len(sb):
                if sa[i] == sb[j]:
                    j += 1
                i += 1
            return j == len(sb)

        for i, s in enumerate(keys):
            if counter[s] > 1: continue    # 若有重复，直接pass
            flag = False
            for j in range(i):    # 判断本串是否是一个更长串的子序列
                if isSub(keys[j], s):
                    flag = True
                    break
            if not flag:
                return len(s)

        return -1