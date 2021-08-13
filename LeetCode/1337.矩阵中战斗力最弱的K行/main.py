#!/usr/bin/env python
from typing import List

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        def search(row):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == 1:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        rows = [(search(row), i) for i, row in enumerate(mat)]
        heapq.heapify(rows)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(rows)[1])
        return res
