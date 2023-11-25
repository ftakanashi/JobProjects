#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def check(time):
            total = 0
            for r in ranks:
                total += math.floor(math.sqrt(time / r))
            return total >= cars

        l, r = 0, ranks[0] * cars * cars
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l