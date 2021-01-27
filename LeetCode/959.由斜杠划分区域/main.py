#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
            self.count += 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.fa[root_x] = root_y
            else:
                self.fa[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1
            self.count -= 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                base = 4 * (i * n + j)
                if grid[i][j] == '/':
                    uf.union(base, base + 3)
                    uf.union(base + 1, base + 2)
                elif grid[i][j] == '\\':
                    uf.union(base, base + 1)
                    uf.union(base + 2, base + 3)
                else:
                    uf.union(base, base + 1)
                    uf.union(base, base + 2)
                    uf.union(base, base + 3)

                if j < n - 1:
                    right_base = 4 * (i * n + j + 1)
                    uf.union(base + 1, right_base + 3)
                if i < m - 1:
                    down_base = 4 * ((i+1) * n + j)
                    uf.union(base + 2, down_base)

        return uf.count