#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.fa[root_x] = root_y
        else:
            self.fa[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

class Solution:
    def isSimilar(self, a: str, b: str) -> bool:
        i = 0
        c = 0
        while i < len(a):
            if a[i] != b[i]: c += 1
            if c > 2: return False
            i += 1
        return c == 0 or c == 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                sa, sb = strs[i], strs[j]
                if uf.find(i) != uf.find(j) and self.isSimilar(sa, sb):
                    uf.union(i, j)

        return sum([1 if uf.find(i) == i else 0 for i in range(n)])