#!/usr/bin/env python
from typing import List
from collections import defaultdict

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for a,b in relation:
            graph[a].append(b)

        queue = deque()
        ans = 0
        queue.append((0, 0))
        while queue:
            node, times = queue.popleft()
            if times >= k:
                if node == n-1 and times == k: ans += 1
                continue

            for nxt in graph[node]:
                queue.append((nxt, times+1))

        return ans