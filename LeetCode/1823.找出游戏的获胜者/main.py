#!/usr/bin/env python

from collections import deque

class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n+1))
        while len(queue) > 1:
            for _ in range(k-1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue.popleft()

class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = ((k - 1) % i + 1 + ans) % i
        return ans + 1