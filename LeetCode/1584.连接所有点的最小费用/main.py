#!/usr/bin/env python
from typing import List

class UnionFind:    # 带有rank优化的并查集
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.fa[root_x] = root_y
            else:
                self.fa[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # 整理所有边并按照cost的升序排序
        dist = lambda x,y: abs(x[0]-y[0]) + abs(x[1]-y[1])
        uf = UnionFind()
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                edges.append((dist(points[i], points[j]), i, j))
        edges.sort(key=lambda x:x[0])

        # 构建图
        cost = 0
        for c, i, j in edges:
            if uf.find(i) != uf.find(j):    # 非同一连通分量时，并查集合并并且cost加上c
                uf.union(i, j)
                cost += c
        return cost

import heapq
class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(p) for p in points]

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        queue = []
        p = points[0]
        visited = set([p,])
        for i in range(1, len(points)):
            heapq.heappush(queue, (dist(p, points[i]), p, points[i]))

        res = 0
        while queue and len(visited) < len(points):
            edge, a, b = heapq.heappop(queue)
            if b in visited: continue
            res += edge
            visited.add(b)
            for p in points:
                if p not in visited: heapq.heappush(queue, (dist(b, p), b, p))
        return res