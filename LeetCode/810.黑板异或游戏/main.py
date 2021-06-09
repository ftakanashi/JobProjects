#!/usr/bin/env python
from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) & 1 == 0: return True
        s = 0
        for n in nums: s = s ^ n
        return s == 0