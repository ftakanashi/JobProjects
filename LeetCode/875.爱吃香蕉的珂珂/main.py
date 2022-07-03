#!/usr/bin/env python
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(speed):
            s = sum([(p // speed) + min(1, p % speed) for p in piles])
            return s <= h

        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l