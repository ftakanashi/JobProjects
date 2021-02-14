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
            if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)

        h2pos = {}
        for i in range(n):
            for j in range(n):
                h2pos[grid[i][j]] = (i, j)    # 事先保存高度 -> 位置的对应信息

        direcs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for t in range(n * n):
            i, j = h2pos[t]
            for a, b in direcs:
                if 0 <= i + a < n and 0 <= j + b < n and grid[i+a][j+b] < t:
                    uf.union(i*n+j, (i+a)*n+j+b)
            if uf.find(0) == uf.find(n*n-1):
                return t

        return -1