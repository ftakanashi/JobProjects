#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        heap = []
        xor = [0 for _ in range(n)]
        for i in range(m):
            x = 0
            for j in range(n):
                x = x ^ matrix[i][j]
                xor_x = x ^ xor[j]
                xor[j] = xor_x
                if len(heap) < k:
                    heapq.heappush(heap, xor_x)
                elif len(heap) == k and xor_x > heap[0]:
                    heapq.heapreplace(heap, xor_x)

        return heap[0]