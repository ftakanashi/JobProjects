#!/usr/bin/env python
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mem = {0: -1}
        ans = diff = 0
        for i, num in enumerate(nums):
            diff += 1 if num == 0 else -1
            if diff in mem:
                ans = max(ans, i - mem[diff])
            else:
                mem[diff] = i
        return ans