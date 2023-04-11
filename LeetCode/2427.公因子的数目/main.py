#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd = math.gcd(a, b)
        ans = 0
        for i in range(1, int(math.sqrt(gcd)) + 1):
            if gcd % i == 0:
                if gcd == i * i:
                    ans += 1
                else:
                    ans += 2
        return ans