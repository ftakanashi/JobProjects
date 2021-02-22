#!/usr/bin/env python
from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        prefix, suffix = [], []
        n = len(a)

        p = 1
        for i in range(n):
            p *= a[i]
            prefix.append(p)
        p = 1
        for i in range(n-1, -1, -1):
            p *= a[i]
            suffix.append(p)
        suffix.reverse()

        res = []
        for i in range(n):
            p_left = 1 if i-1 < 0 else prefix[i-1]
            p_right = 1 if i+1 >= n else suffix[i+1]
            res.append(p_left * p_right)
        return res