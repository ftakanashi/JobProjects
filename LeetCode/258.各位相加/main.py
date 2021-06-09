#!/usr/bin/env python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        remind = num % 9
        return 9 if remind == 0 else remind