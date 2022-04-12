#!/usr/bin/env python
from typing import List

from collections import defaultdict, deque

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # 构建图
        n = len(patience)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # BFS计算单源最短路径
        dist = [float('inf') for _ in range(n)]
        dist[0] = 0
        queue = deque()
        for nxt in graph[0]: queue.append((nxt, 1))
        while queue:
            node, d = queue.popleft()
            if d < dist[node]:
                dist[node] = d
                for nxt in graph[node]: queue.append((nxt, d + 1))

        # 计算全局最大值
        ans = 0
        for i in range(1, n):
            d, p = dist[i], patience[i]
            times = (d * 2) // p if (d * 2) % p != 0 else (d * 2) // p - 1
            ans = max(ans, times * p + 2 * d)
        return ans + 1