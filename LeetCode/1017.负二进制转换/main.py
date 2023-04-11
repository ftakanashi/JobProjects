#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1: return str(n)
        digits = []
        while n != 0:
            reminder = n % 2
            digits.append(reminder)
            n = (n - reminder) // -2

        return "".join([str(d) for d in reversed(digits)])