#!/usr/bin/env python
from typing import List

import collections
import heapq

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        num_and_count = [(-i, n) for n, i in counter.items()]
        heapq.heapify(num_and_count)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(num_and_count)[1])
        return res