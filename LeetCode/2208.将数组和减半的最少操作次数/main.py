#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        s = sum(nums)
        rest, tgt = s, s / 2
        ans = 0
        while rest > tgt:
            curr = heapq.heappop(heap) *  -1
            half = curr / 2
            rest -= half
            heapq.heappush(heap, half * -1)
            ans += 1
        return ans