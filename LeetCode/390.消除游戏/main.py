#!/usr/bin/env python

class Solution:
    def lastRemaining(self, n: int) -> int:
        a, d, n = 1, 1, n
        rev = False
        while n > 1:
            if not rev or n & 1 == 1:
                a += d    # 只有逆向扫描且项数为偶数时，才会保留a0
            n = n // 2
            d *= 2
            rev = not rev
        return a