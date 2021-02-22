#!/usr/bin/env python
from typing import List

import collections

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        queue = collections.deque([])
        count = 0
        n = len(A)
        for i in range(n):
            if queue and i - queue[0] >= K: queue.popleft()
            if (A[i] + len(queue)) & 1 == 0:
                if i > n - K: return -1
                count += 1
                queue.append(i)
        return count