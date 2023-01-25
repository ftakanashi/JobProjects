#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n - 2):
            counter = Counter(s[i:i+2])
            max_v = max(counter.values())
            for j in range(i + 2, n):
                counter[s[j]] += 1
                max_v = max(max_v, counter[s[j]])
                ans += (max_v - min(counter.values()))
        return ans