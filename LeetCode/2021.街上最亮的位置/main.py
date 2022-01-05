#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)
        for center, r in lights:
            left, right = center - r, center + r
            diff[left] += 1
            diff[right + 1] -= 1

        ans_pos, ans_s = None, 0
        s = 0
        for pos in sorted(diff):
            s += diff[pos]
            if s > ans_s:
                ans_s, ans_pos = s, pos
        return ans_pos