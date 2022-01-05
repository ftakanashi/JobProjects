#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.cnt = 0

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
            self.cnt += 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.cnt -= 1
            if self.rank[rx] < self.rank[ry]:
                self.fa[rx] = ry
            else:
                self.fa[ry] = rx
                if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1

    def getCount(self):
        return self.cnt

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(n):
            uf.find(i)
        for a, b in edges:
            uf.union(a, b)
        return uf.getCount()