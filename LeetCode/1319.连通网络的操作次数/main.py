#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

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
            if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for con in connections:
            uf.union(*con)

        count = sum([1 if i == uf.fa[i] else 0 for i in range(n)])
        return count - 1