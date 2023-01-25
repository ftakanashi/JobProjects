#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        digits = []
        while n > 0:
            digits.append(n % 3)
            n = n // 3
        for d in digits:
            if d == 2: return False
        return True