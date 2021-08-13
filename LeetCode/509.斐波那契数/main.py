#!/usr/bin/env python

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        i = 2
        a, b = 0, 1
        while i <= n:
            s = a + b
            a, b = b, s
            i += 1
        return b