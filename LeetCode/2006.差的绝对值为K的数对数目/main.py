#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for num in counter:
            if num - k in counter:
                ans += counter[num] * counter[num - k]
            if num + k in counter:
                ans += counter[num] * counter[num + k]
        return ans // 2