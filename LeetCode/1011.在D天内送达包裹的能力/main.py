#!/usr/bin/env python

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def able(cap):
            d, cur = D, 0
            for w in weights:
                cur += w
                if cur > cap:
                    cur = w
                    d -= 1
                    if d == 0: return False
            return True

        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if able(mid): r = mid - 1
            else: l = mid + 1
        return l
