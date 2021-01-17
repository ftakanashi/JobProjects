#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        r = x
        while r != self.fa[r]:
            r = self.fa[r]

        while x != self.fa[x]:
            tmp = self.fa[x]
            self.fa[x] = r
            x = tmp
        return r

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x < root_y:
            self.fa[root_y] = root_x
        elif root_x > root_y:
            self.fa[root_x] = root_y

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for x, y in edges:    # 注意题目给出的是序号不是下标
            if uf.find(x - 1) != uf.find(y - 1):
                uf.union(x - 1, y - 1)
            else:
                return [x, y]
        return []