#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums: return 0
        min_heap, max_heap = [], []
        l, r, max_len = 0, 0, 0

        while r < len(nums):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-nums[r], r))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                if nums[l] == -max_heap[0][0]:
                    while max_heap[0][1] <= l: heapq.heappop(max_heap)
                if nums[l] == min_heap[0][0]:
                    while min_heap[0][1] <= l: heapq.heappop(min_heap)
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len