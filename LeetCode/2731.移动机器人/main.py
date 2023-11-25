#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n, MOD = len(nums), 10 ** 9 + 7
        pos = [nums[i] + (d if s[i] == "R" else -d) for i in range(n)]
        pos.sort()
        ans = 0
        for i in range(1, n):
            gap = pos[i] - pos[i - 1]
            ans += (gap * i * (n - i)) % MOD
        return ans % MOD