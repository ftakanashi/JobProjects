#!/usr/bin/env python

class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 and y > 0:
            dist += (x&1)^(y&1)
            x = x >> 1
            y = y >> 1
        while x > 0:
            dist += x & 1
            x = x >> 1
        while y > 0:
            dist += y & 1
            y = y >> 1
        return dist

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        while xor > 0:
            dist += 1
            xor = (xor & (xor - 1))
        return dist