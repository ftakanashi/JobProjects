#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def printBin(self, num: float) -> str:
        ans = "0."
        while len(ans) <= 32 and num > 0:
            num *= 2
            digit = int(num)
            ans += str(digit)
            num -= digit
        return ans if len(ans) <= 32 else "ERROR"