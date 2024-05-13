#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        cnt = Counter(changed)
        if len(changed) & 1 == 1 or cnt[0] & 1 == 1: return ans
        changed.sort()

        for n in changed:
            if cnt[n] == 0: continue
            if cnt[n * 2] == 0: return []
            cnt[n] -= 1
            cnt[n * 2] -= 1
            ans.append(n)

        return ans