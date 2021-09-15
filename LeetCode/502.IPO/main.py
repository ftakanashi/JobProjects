#!/usr/bin/env python
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        items = [(c, -p) for (c, p) in zip(capital, profits)]
        items.sort(reverse=True)
        heap = []
        while k > 0:
            while items and items[-1][0] <= w:
                c, p = items.pop()
                heapq.heappush(heap, p)
            if heap:
                w += -heapq.heappop(heap)
                k -= 1
            else:
                break
        return w