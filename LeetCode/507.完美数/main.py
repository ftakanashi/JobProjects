#!/usr/bin/env python

class Solution1:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        s = 1
        a = 2
        while a * a <= num:
            if num % a == 0:
                s += a
                if a * a != num: s += (num // a)
            a += 1
        return num == s

class Solution2:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]