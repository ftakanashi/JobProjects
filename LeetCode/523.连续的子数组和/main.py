#!/usr/bin/env python
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = [0, ]
        mem = {0: -1}
        for i, num in enumerate(nums):
            s = presum[-1] + num
            presum.append(s)
            remind = s % k
            if remind not in mem:
                mem[remind] = i
            elif i - mem[remind] >= 2:
                return True
        return False