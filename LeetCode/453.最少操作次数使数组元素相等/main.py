#!/usr/bin/env python
from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        min_v = min(nums)
        for num in nums:
            ans += (num - min_v)
        return ans