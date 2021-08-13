#!/usr/bin/env python
from typing import List

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        F = float('inf')
        graph = [[F for _ in range(n)] for _ in range(n)]
        for start, end, edge in times:
            graph[start-1][end-1] = edge

        heap = [(0, k-1)]
        dist = [F for _ in range(n)]
        while heap:
            d, node = heapq.heappop(heap)
            if dist[node] <= d: continue
            dist[node] = d
            for nxt_node, nxt_edge in enumerate(graph[node]):
                if nxt_edge < F:
                    heapq.heappush(heap, (d + nxt_edge, nxt_node))

        return -1 if max(dist) is F else max(dist)