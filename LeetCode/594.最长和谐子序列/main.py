#!/usr/bin/env python
from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for num in counter.keys():
            if num - 1 in counter:
                ans = max(ans, counter[num-1] + counter[num])
            if num + 1 in counter:
                ans = max(ans, counter[num] + counter[num + 1])
        return ans