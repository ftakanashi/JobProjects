#!/usr/bin/env python

from typing import List
from functools import lru_cache as cache

class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        finished = set()

        @cache
        def dfs(node):
            if node in finished: return True
            if node in visited: return False
            visited.add(node)
            for nxt in graph[node]:
                if not dfs(nxt): return False
            finished.add(node)
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i): res.append(i)
        return res

from collections import deque
class Solution2:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                rev_graph[y].append(x)
        in_deg = [len(ys) for ys in graph]

        q = deque([i for i, d in enumerate(in_deg) if d == 0])    # 初始化队列，将所有0入度节点作为出发点
        while q:
            node = q.popleft()
            for x in rev_graph[node]:
                in_deg[x] -= 1
                if in_deg[x] == 0:
                    q.append(x)

        return [i for i, d in enumerate(in_deg) if d == 0]