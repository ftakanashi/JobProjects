#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        num1 = num2 = ""
        for i in range(0, len(digits), 2):
            num1 += digits[i]
            if i + 1 < len(digits):
                num2 += digits[i+1]

        return int(num1) + int(num2)