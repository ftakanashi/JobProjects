#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1

        for i in range(n):
            a, b = b, a + b

        return a if a <= (1e9 + 7) else a % int(1e9 + 7)