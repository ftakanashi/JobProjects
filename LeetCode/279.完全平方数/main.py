#!/usr/bin/env python
import collections

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(101)]
        queue = collections.deque([])
        queue.append((n, 0, len(squares) - 1))
        while len(queue) > 0:
            rest, count, max_i = queue.popleft()
            if rest == 0: return count
            for i in range(max_i, -1, -1):
                if squares[i] > rest: continue
                queue.append((rest - squares[i], count + 1, i))
        return -1