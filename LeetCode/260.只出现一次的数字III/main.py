#!/usr/bin/env python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = 0
        for num in nums:
            s = s ^ num
        mask = 1
        while s & mask == 0:    # 寻找一个是1的位置
            mask = mask << 1
        g0, g1 = 0, 0
        for num in nums:
            if num & mask == 0:
                g0 = g0 ^ num
            else:
                g1 = g1 ^ num
        return [g0, g1]