#!/usr/bin/env python
from collections import deque

class Solution:
    def integerReplacement(self, n: int) -> int:
        seen = set()
        queue = deque()
        queue.append((n, 0))
        while queue:
            num, times = queue.popleft()
            if num == 1: return times
            seen.add(num)
            if num & 1 == 1:
                if num + 1 not in seen:
                    queue.append((num + 1, times + 1))
                if num - 1 not in seen:
                    queue.append((num - 1, times + 1))
            else:
                if num // 2 not in seen:
                    queue.append((num // 2, times + 1))
        return -1