#!/usr/bin/env python

class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = []
        for ch in number:
            if ch in (" ", "-"): continue
            digits.append(ch)

        n = len(digits)
        i = 0
        ans = ""
        while n > 4:
            ans += "".join(digits[i:i + 3])
            ans += "-"
            n -= 3
            i += 3

        if n < 4:
            ans += "".join(digits[i:])
        else:
            ans += "".join(digits[i:i + 2]) + "-" + "".join(digits[i + 2:])

        return ans