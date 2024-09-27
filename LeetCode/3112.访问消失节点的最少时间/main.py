#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import heapq

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b, cost in edges:
            graph[a].append((cost, b))
            graph[b].append((cost, a))

        dist = [99999 for _ in range(n)]
        heap = [(0, 0)]
        while len(heap) > 0:
            cost, node = heapq.heappop(heap)
            if dist[node] <= cost: continue
            if disappear[node] <= cost: continue
            dist[node] = cost
            for nxt_cost, nxt_node in graph[node]:
                if dist[nxt_node] > nxt_cost + cost:
                    heapq.heappush(heap, (nxt_cost + cost, nxt_node))

        return [i if i < 99999 else -1 for i in dist]
