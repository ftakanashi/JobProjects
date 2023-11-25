#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        ans = 0
        while k > 0:
            num = heapq.heappop(heap)
            div = (-num + 2) // 3
            ans += -num
            heapq.heappush(heap, -div)
            k -= 1
        return ans