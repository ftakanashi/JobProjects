#!/usr/bin/env python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        base = n & 1
        while n > 0:
            if n & 1 != base: return False
            base = base ^ 1
            n = n >> 1
        return True