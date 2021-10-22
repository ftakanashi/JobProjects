#!/usr/bin/env python
class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        base = 1
        while num > 0:
            ans = ans + ((num & 1) ^ 1) * base
            base = base << 1
            num = num >> 1
        return ans