#!/usr/bin/env python
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x & 1)
        return nums