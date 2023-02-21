#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def contrib(y, x):
            return -((x - y) / (x * (x + 1)))

        heap = [(contrib(y, x), y, x) for y, x in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            score, y, x = heapq.heappop(heap)
            x += 1
            y += 1
            heapq.heappush(
                heap,
                (contrib(y, x), y, x)
            )

        return sum([item[1]/item[2] for item in heap]) / len(heap)