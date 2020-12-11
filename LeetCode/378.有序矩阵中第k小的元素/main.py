#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        flat = []
        for i in range(n):
            for j in range(n):
                flat.append(matrix[i][j])
        flat.sort()
        return flat[k-1]

import heapq
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]