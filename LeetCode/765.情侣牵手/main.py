#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.size = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0
            self.size[x] = 1
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[x] < self.rank[y]:
                self.fa[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.fa[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        p2i = {n: i//2 for i, n in enumerate(row)}
        uf = UnionFind()
        for p in row:
            if p & 1 == 0:
                uf.union(p2i[p], p2i[p+1])
            else:
                uf.union(p2i[p], p2i[p-1])

        count = 0
        for sofa in uf.fa:
            if uf.find(sofa) == sofa:
                count += (uf.size[sofa] - 1)
        return count