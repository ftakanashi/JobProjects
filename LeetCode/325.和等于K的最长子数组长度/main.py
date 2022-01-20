#!/usr/bin/env python
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = [0, ]
        for num in nums:
            presum.append(presum[-1] + num)

        mapping = {}
        ans = 0
        for i, s in enumerate(presum):
            if s not in mapping:
                mapping[s] = i
            if s - k in mapping:
                ans = max(ans, i - mapping[s-k])
        return ans