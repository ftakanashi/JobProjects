#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def myPow(self, x: float, n: int) -> float:
        minus = False
        if n < 0:
            n = -n
            minus = True

        if n == 0: return 1

        half = self.myPow(x, n >> 1)
        if n & 1 == 1:
            res = half * half * x
        else:
            res = half * half

        return 1 / res if minus else res