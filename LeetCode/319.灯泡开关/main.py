#!/usr/bin/env python

class Solution:
    def bulbSwitch(self, n: int) -> int:
        ans = 0
        num = 1
        while num * num <= n:
            ans += 1
            num += 1
        return ans