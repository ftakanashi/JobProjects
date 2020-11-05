#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        dig = 9    # 记录n位数中的符合要求的数字个数
        res = 10    # 记录累计的符合要求的数字个数总和
        for i in range(2, 11):
            dig *= 11 - i
            res += dig
            if i == n: return res

        return res