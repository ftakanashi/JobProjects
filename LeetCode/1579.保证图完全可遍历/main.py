#!/usr/bin/env python
from typing import List
import copy

class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.comp_count = n
        self.remove_edge = 0

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            self.remove_edge += 1
        else:
            self.comp_count -= 1
            if self.rank[root_x] < self.rank[root_y]:
                self.fa[root_x] = root_y
            else:
                self.fa[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        # 基于公用边的图构建
        for t, a, b in edges:
            a, b = a - 1, b - 1
            if t != 3: continue
            uf.union(a, b)

        # 创建两个副本分别作为Alice和Bob的图
        ufa = copy.deepcopy(uf)
        ufb = copy.deepcopy(uf)
        for t, a, b in edges:
            a, b = a - 1, b - 1
            if t == 1:
                ufa.union(a, b)
            elif t == 2:
                ufb.union(a, b)

        if ufa.comp_count > 1 or ufb.comp_count > 1:
            return -1
        return ufa.remove_edge + ufb.remove_edge - uf.remove_edge