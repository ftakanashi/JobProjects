#!/usr/bin/env python
from typing import List
from collections import deque

class Solution1:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        seen = set()
        queue = deque()

        for i in range(n):
            queue.append((i, 1 << i, 0))

        while queue:
            node, mask, dist = queue.popleft()
            if (node, mask) in seen: continue
            seen.add((node, mask))
            if mask == (1 << n) - 1: return dist
            for nxt in graph[node]:
                queue.append((nxt, mask | (1 << nxt), dist + 1))

        return -1