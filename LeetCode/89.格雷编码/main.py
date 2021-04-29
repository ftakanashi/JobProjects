#!/usr/bin/env python

from typing import List

class Solution:
    def grayCode(self, N: int) -> List[int]:
        if N == 0: return [0]

        def rec(n):
            if n == 1: return [0, 1]
            res = []
            prev_nums = rec(n - 1)
            for num in prev_nums:
                if not res or res[-1] & 1 == 0:
                    res.append(num * 2)
                    res.append(num * 2 + 1)
                else:
                    res.append(num * 2 + 1)
                    res.append(num * 2)
            return res

        return rec(N)