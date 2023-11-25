#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import defaultdict
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        ans = float("inf")
        for i in range(1, n + 1):
            for j in range(i):
                for k in range(j):
                    if j in graph[i] and k in graph[i] and k in graph[j]:
                        ans = min(ans, len(graph[i]) + len(graph[j]) + len(graph[k]) - 6)

        return ans if ans < float("inf") else -1