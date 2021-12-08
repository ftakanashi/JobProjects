#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while nums[0] < 0 and k > 0:
            num = heapq.heappop(nums)
            heapq.heappush(nums, -num)
            k -= 1
        if nums[0] >= 0:
            if k & 1 == 1: nums[0] *= -1
        return sum(nums)