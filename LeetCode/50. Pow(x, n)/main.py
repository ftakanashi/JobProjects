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

class Solution2:
    '''
    一种更加方便记忆的，递推式的快速幂
    '''
    def myPow(self, x: float, n: int) -> float:
        minus = False
        if n < 0:
            n = -n
            minus = True

        res = 1
        while n > 0:
            if n & 1 == 1:
                res *= x
            x *= x
            n = n >> 1

        return 1 / res if minus else res