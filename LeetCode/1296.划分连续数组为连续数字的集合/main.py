#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        nums.sort()
        counter = Counter(nums)

        i = 0
        while i < n:
            if counter[nums[i]] > 0:
                for h in range(nums[i], nums[i] + k):
                    counter[h] -= 1
                    if counter[h] < 0: return False
            i += 1
        return True