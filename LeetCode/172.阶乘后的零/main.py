#!/usr/bin/env python

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(0, n+1, 5):

            while i > 0 and i % 5 == 0:
                i = i // 5
                count += 1

        return count