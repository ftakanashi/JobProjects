#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        info = []
        for ch in s:
            if not info or info[-1][0] != ch:
                info.append([ch, 1])
            else:
                info[-1][1] += 1

        ans = 0
        for ch, cnt in info:
            ans += ((cnt * (cnt + 1)) // 2) % MOD
        return ans