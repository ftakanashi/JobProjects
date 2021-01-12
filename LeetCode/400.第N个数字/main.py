#!/usr/bin/env python

class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        s = 0
        while n > s:
            i += 1
            s += (9 * pow(10, i-1) * i)

        k = 0
        base = 0
        while k < i - 1:
            k += 1
            base += (9 * pow(10, k-1) * k)

        num = (((n - base - 1) // i)) + pow(10, i-1)
        dig = (n - base) % i
        return str(num)[dig-1]