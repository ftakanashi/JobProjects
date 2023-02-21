#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a, b, c = amount
        ans = 0
        while a > 0 and b > 0 and c > 0:
            if a >= c and b >= c:
                a -= 1
                b -= 1
            elif a >= b and c >= b:
                a -= 1
                c -= 1
            elif b >= a and c >= a:
                b -= 1
                c -= 1
            ans += 1

        ans += max([a, b, c])
        return ans