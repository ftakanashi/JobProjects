#!/usr/bin/env python
from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r, s, res = 1, 0, 0, []
        while r <= (target + 1) // 2:
            while s <= target:
                if s == target: res.append(list(range(l, r + 1)))
                r += 1
                s += r
            while s > target:
                s -= l
                l += 1
        return res