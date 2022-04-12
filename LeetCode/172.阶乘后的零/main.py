#!/usr/bin/env python

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(0, n+1, 5):

            while i > 0 and i % 5 == 0:
                i = i // 5
                count += 1

        return count

class Solution_20220325:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        base = 5
        while n >= base:
            count += (n // base)
            base *= 5
        return count