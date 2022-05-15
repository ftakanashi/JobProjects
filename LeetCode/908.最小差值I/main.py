#!/usr/bin/env python
from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if min_val + k < max_val - k:
            return max_val - min_val - 2 * k
        else:
            return 0