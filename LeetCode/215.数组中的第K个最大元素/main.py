#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_nums = [-n for n in nums]
        heapq.heapify(rev_nums)
        for _ in range(k - 1):
            heapq.heappop(rev_nums)
        return -rev_nums[0]