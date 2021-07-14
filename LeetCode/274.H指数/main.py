#!/usr/bin/env python

import heapq
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heap = [-i for i in citations]
        heapq.heapify(heap)
        cnt = 1
        while heap:
            num = heapq.heappop(heap)
            if -num < cnt: break
            cnt += 1
        return cnt - 1