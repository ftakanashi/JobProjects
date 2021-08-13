#!/usr/bin/env python

from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return
        if self.rank[rx] < self.rank[ry]:
            self.fa[rx] = ry
        else:
            self.fa[ry] = rx
            if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        points = []
        for i in range(m):
            for j in range(n):
                points.append((grid[i][j], i, j))
        points.sort()    # 升序排序，后面直接从末尾pop，就可以获得倒序序列了

        # 后续遍历不涉及起点和终点本身，所以这里ans与seen的初始化都要考虑这两者
        seen = set()
        ans = min(grid[0][0], grid[m-1][n-1])
        seen.add((0, 0))
        seen.add((m - 1, n - 1))
        uf = UnionFind()

        direc = [(0,1), (0,-1), (1,0), (-1,0)]
        while uf.find((0, 0)) != uf.find((m-1, n-1)):
            v, x, y = points.pop()
            ans = min(ans, v)
            seen.add((x, y))
            for a, b in direc:
                nx, ny = x+a, y+b
                if (nx, ny) in seen:
                    uf.union((x, y), (nx, ny))
        return ans