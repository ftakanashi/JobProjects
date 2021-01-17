#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        self.fa[self.find(x)] = self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        n = len(stones)
        for x, y in stones:
            uf.union(x, y + 10000)

        return n - sum([1 if uf.fa[i] == i else 0 for i in uf.fa])