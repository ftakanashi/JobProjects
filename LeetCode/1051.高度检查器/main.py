#!/usr/bin/env python
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = list(sorted(heights))
        ans = 0
        for i, (a, b) in enumerate(zip(heights, sorted_h)):
            if a != b: ans += 1
        return ans