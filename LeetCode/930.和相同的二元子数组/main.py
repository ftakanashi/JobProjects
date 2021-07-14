#!/usr/bin/env python
from typing import List
from collections import Counter

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = ans = 0
        counter = Counter([0,])
        for num in nums:
            s += num
            if s - goal in counter:
                ans += counter[s - goal]
            counter[s] += 1
        return ans