#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        l, r = 1, target
        while l <= r:
            mid = (l + r) // 2
            s = (1 + mid) * mid // 2
            if s < target:
                l = mid + 1
            elif s > target:
                r = mid - 1
            else:
                return mid
        # 此时的l是我们要找的 `x`
        return l if ((1 + l) * l // 2 - target) & 1 == 0 else l + 1 + (l & 1)