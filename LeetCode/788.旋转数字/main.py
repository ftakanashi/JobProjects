#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import cache

class Solution:
    @cache
    def check(self, num: int) -> int:
        if num < 10:
            if num in (2, 5, 6, 9):
                return 1
            elif num in (0, 1, 8):
                return 0
            else:
                return -1
        pre_flag, suf_flag = self.check(num // 10), self.check(num % 10)
        if pre_flag < 0 or suf_flag < 0: return -1
        if pre_flag > 0 or suf_flag > 0: return 1
        return 0

    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.check(i) > 0:
                ans += 1
        return ans