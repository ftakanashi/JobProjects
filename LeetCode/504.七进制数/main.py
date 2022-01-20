#!/usr/bin/env python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        minus = num < 0
        num = abs(num)
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num = num // 7

        ans = "".join(reversed(digits))
        if minus:
            ans = "-" + ans
        return ans