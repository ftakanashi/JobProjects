#!/usr/bin/env python
from typing import List
from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counter = Counter([0, ])
        s = 0
        ans = 0
        for num in nums:
            s += (num & 1)
            ans += (counter[s - k])
            counter[s] += 1
        return ans