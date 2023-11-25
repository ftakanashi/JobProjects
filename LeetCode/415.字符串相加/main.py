#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        p1, p2 = len(num1) - 1, len(num2) - 1
        remind = 0
        ans = ""
        while p1 >= 0 and p2 >= 0:
            tmp = int(num1[p1]) + int(num2[p2]) + remind
            digit, remind = tmp % 10, tmp // 10
            ans = str(digit) + ans
            p1 -= 1
            p2 -= 1

        while p1 >= 0:
            tmp = int(num1[p1]) + remind
            digit, remind = tmp % 10, tmp // 10
            ans = str(digit) + ans
            p1 -= 1

        if remind > 0:
            ans = str(remind) + ans

        return ans