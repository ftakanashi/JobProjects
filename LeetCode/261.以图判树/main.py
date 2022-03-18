#!/usr/bin/env python
from typing import List

class UnionFind:
    '''
    标准哈希实现的并查集，追加了一个cnt用于维护并查集中不同连通分量的数量
    '''
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
        if rx == ry: return
        self.cnt -= 1
        if self.rank[rx] < self.rank[ry]:
            self.fa[rx] = ry
        else:
            self.fa[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        uf = UnionFind()
        for a, b in edges:
            if uf.find(a) == uf.find(b):
                return False
            uf.union(a, b)
        return all(i in uf.fa for i in range(n)) and uf.cnt == 1
