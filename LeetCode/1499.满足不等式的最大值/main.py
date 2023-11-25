#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        ans = float("-inf")
        for xj, yj in points:
            while heap and (xj - heap[0][1]) > k:
                heapq.heappop(heap)
            if heap:
                ans = max(ans, xj + yj - heap[0][0])
            heapq.heappush(heap, ((xj - yj), xj))

        return ans