#!/usr/bin/env python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for n in nums[:k+1]:
            if n in seen: return True
            seen.add(n)

        i, j = 0, k + 1
        while j < len(nums):
            seen.remove(nums[i])
            if nums[j] in seen: return True
            seen.add(nums[j])
            i += 1
            j += 1

        return False