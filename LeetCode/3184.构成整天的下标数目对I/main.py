#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = Counter()
        for h in hours:
            cnt[h % 24] += 1
        ans = cnt[0] * (cnt[0] - 1) // 2 + cnt[12] * (cnt[12] - 1) // 2
        for n in sorted(cnt):
            if n == 0: continue
            if cnt[24 - n] > 0 and 24 - n > n:
                ans += (cnt[n] * cnt[24 - n])
        return ans