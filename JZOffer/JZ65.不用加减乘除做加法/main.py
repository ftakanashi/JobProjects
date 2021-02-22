#!/usr/bin/env python
class Solution:
    def add(self, a: int, b: int) -> int:
        if b == 0: return a if a <= 2**31-1 else (a % 2**32) - 2**32
        x = (a ^ b) % 2**32
        y = a & b
        y = 0 if y > 2**31 else y << 1
        return self.add(x, y)