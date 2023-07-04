#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = list(counter.keys())
        if len(keys) < 3: return 0
        ans = 0
        n = len(keys)

        # 也可以这样：
        # for a, b, c in itertools.combinations(keys, 3):
        #     ans += counter[a] * counter[b] * counter[c]

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    a, b, c = keys[i], keys[j], keys[k]
                    ans += counter[a] * counter[b] * counter[c]

        return ans