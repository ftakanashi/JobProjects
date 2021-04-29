#!/usr/bin/env python

from typing import List

import bisect

class Solution1:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = -1
        while i < j:
            if nums[i] + nums[j] >= k:
                j -= 1
            else:
                ans = max(ans, nums[i] + nums[j])
                i += 1
        return ans

class Solution2:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        for i, n in enumerate(nums):
            if n >= k: break

            j = bisect.bisect_left(nums, k - n) - 1
            if j > 0 and j != i:
                ans = max(ans, nums[j] + n)

        return ans