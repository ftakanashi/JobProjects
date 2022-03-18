#!/usr/bin/env python
from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2: return "/".join([str(n) for n in nums])
        nums.append(")")
        nums.insert(1, "(")
        return "/".join([str(n) for n in nums]).replace("(/", "(").replace("/)", ")")