#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import defaultdict, deque

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in paths:
            graph[a].add(b)
            graph[b].add(a)
        colors = [0 for _ in range(n + 1)]

        q = deque(list(range(1, n + 1)))
        while q:
            node = q.popleft()
            if colors[node] > 0: continue
            adj_colors = {colors[i] for i in graph[node]}
            for color in (1, 2, 3, 4):
                if color in adj_colors: continue
                colors[node] = color
                break
            for nxt in graph[node]:
                q.append(nxt)

        return colors[1:]
