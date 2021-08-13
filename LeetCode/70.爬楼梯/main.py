#!/usr/bin/env python

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n
        a, b = 1, 2
        for _ in range(3, n+1):
            tmp = b
            b = a + b
            a = tmp
        return b