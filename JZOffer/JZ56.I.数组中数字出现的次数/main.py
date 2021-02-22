#!/usr/bin/env python
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        t = 0
        for n in nums:
            t = n ^ t

        digit = 0
        while t & 1 == 0:
            t = t >> 1
            digit += 1

        t_a, t_b = 0, 0
        pivot = 1 << digit
        for n in nums:
            if n & pivot > 0:
                t_a = t_a ^ n
            else:
                t_b = t_b ^ n
        return t_a, t_b