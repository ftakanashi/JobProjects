#!/usr/bin/env python
from typing import List

class UnionFind:
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
        if root_x == root_y: return
        if self.rank[root_x] < self.rank[root_y]:
            self.fa[root_x] = root_y
        else:
            self.fa[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind()
        parents = [i for i in range(n+1)]    # 初始化parents数组。每个节点的parents都是自己
        conflict_edge = cycle_edge = -1
        for i, (a, b) in enumerate(edges):
            if parents[b] != b:    # 说明父节点已经不是初始化状态，已经被修改，即检测到冲突边
                conflict_edge = i
            else:
                parents[b] = a
                if uf.find(a) == uf.find(b):
                    cycle_edge = i    # 检测到成环边
                else:
                    uf.union(a, b)

        # 按照md中说的，对三种情况进行分类讨论。
        if conflict_edge < 0:
            return edges[cycle_edge]
        elif cycle_edge < 0:
            return edges[conflict_edge]
        else:
            b = edges[conflict_edge][1]
            return [parents[b], b]