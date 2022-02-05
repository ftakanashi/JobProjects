#!/usr/bin/env python
from typing import List

from math import sqrt
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def dfs(num, part):
            start_fac = part[-1] if part else 2
            for i in range(start_fac, int(sqrt(num)) + 1):
                if num % i == 0:
                    dfs(num // i, part + [i,])
            if part:
                res.append(part + [num, ])

        dfs(n, [])
        return res