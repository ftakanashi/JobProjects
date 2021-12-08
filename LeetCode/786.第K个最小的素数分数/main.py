#!/usr/bin/env python
from typing import List

import heapq
class Solution1:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(1, n):
            heapq.heappush(heap, (1/arr[i], 1, arr[i], 0, i))

        for _ in range(k-1):
            _, ai, aj, i, j = heapq.heappop(heap)
            if i < j - 1:
                i += 1
                heapq.heappush(
                    heap,
                    (arr[i]/arr[j], arr[i], arr[j], i, j)
                )

        return [heap[0][1], heap[0][2]]

