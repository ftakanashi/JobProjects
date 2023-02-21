#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 构建图
        graph = defaultdict(lambda: [[], []])
        for i, j in redEdges: graph[i][0].append(j)
        for i, j in blueEdges: graph[i][1].append(j)

        ans = [float('inf') for _ in range(n)]

        queue = deque()
        queue.append((0, 0, 0))    # 第一步走红边的情况
        queue.append((0, 1, 0))    # 第一步走蓝边的情况

        seen = set()
        while queue:
            # 开始BFS
            node, color, dist = queue.popleft()
            seen.add((node, color))    # 走重复路的标志是 节点 + 入边颜色
            next_color = color ^ 1
            ans[node] = min(ans[node], dist)
            for nxt in graph[node][next_color]:
                if (nxt, next_color) in seen: continue
                queue.append((nxt, next_color, dist + 1))

        return [i if i < float("inf") else -1 for i in ans]