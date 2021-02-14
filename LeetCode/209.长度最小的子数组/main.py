#!/usr/bin/env python
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        res = 0
        min_len = float('inf')
        while True:
            if res < s:
                if j == len(nums): break
                res += nums[j]
                j += 1
            else:
                min_len = min(min_len, j - i)
                res -= nums[i]
                i += 1

        return 0 if min_len == float('inf') else min_len