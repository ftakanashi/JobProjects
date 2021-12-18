#!/usr/bin/env python

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = ans = 0
        while full > 0:
            empty += full
            ans += full
            full = empty // numExchange
            empty = empty % numExchange
        return ans