#!/usr/bin/env python
from typing import List

import bisect

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count(t):
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect.bisect_left(nums, num - t, 0, j)    # bisect_left的第三、四个参数也挺有用的
                cnt += j - i
            return cnt

        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            cnt = count(mid)
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1
        return l