#!/usr/bin/env python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            minus = True
        else:
            minus = False

        dividend, divisor = abs(dividend), abs(divisor)

        def rec(a: int, b: int) -> int:
            if a < b: return 0
            if a == b : return 1
            res = 0
            n = b
            i = 1
            while n + n < a:
                n += n
                i += i

            res += i
            res += rec(a - n, b)

            return res

        ans = rec(dividend, divisor)

        if minus and ans > 2**31:
            ans = 2**31
        elif not minus and ans >= 2**31:
            ans = 2**31 - 1

        return -ans if minus else ans