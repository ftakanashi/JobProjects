#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        p = int((2 * candies + 0.25) ** 0.5 - 0.5)
        rest = int(candies - (p + 1) * p * 0.5)
        rows, cols = p // n, p % n

        ans = [0 for _ in range(n)]
        for i in range(n):
            ans[i] = (i + 1) * rows + n * (rows * (rows - 1)) // 2
            if i < cols:
                ans[i] += (i + 1 + (rows * n))

        ans[cols] += rest
        return ans