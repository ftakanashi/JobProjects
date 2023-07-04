#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = Counter([t % 60 for t in time])
        ans = 0
        seen = set()
        for t in cnt:
            if t in seen: continue
            c = cnt[t]
            if t == 0 or t == 30:
                ans += (c * (c - 1) // 2)
            else:
                ans += (c * cnt[60 - t])
            seen.add(t)
            seen.add(60 - t)

        return ans