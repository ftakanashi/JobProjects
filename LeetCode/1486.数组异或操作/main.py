#!/usr/bin/env python

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        e = 1 if n & 1 == start & 1 == 1 else 0

        def f(num):
            res = num
            for i in range(1, (num % 4) + 1):
                res = res ^ (num - i)
            return res

        s = start // 2
        return (f(s-1) ^ f(s+n-1)) * 2 + e