#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def normal_pow(x: float, n: int) -> float:
            if n == 0: return 0 if x == 0 else 1
            if n == 1: return x
            if n & 1 == 1:
                res = normal_pow(x, (n-1) >> 1)
                return res * res * x
            else:
                res = normal_pow(x, n >> 1)
                return res * res

        if n >= 0:
            return normal_pow(x, n)
        else:
            if x == 0: return float('inf')    # 0的负数次方的处理
            return 1 / normal_pow(x, -n)