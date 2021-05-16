#!/usr/bin/env python

from typing import List

import collections
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        presum_counter = collections.Counter()
        for row in wall:
            s = 0
            for brick in row[:-1]:
                s += brick
                presum_counter[s] += 1
        return height - (max(presum_counter.values()) if len(presum_counter) > 0 else 0)