#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        n = ans = 1
        seen = {1, }
        while n > 0:
            n = (n * 10 + 1) % k
            if n in seen: return -1
            seen.add(n)
            ans += 1
        return ans