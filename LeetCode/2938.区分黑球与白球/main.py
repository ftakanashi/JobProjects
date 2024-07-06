#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = zero = 0
        for ch in reversed(s):
            if ch == "0":
                zero += 1
            else:
                ans += zero
        return ans