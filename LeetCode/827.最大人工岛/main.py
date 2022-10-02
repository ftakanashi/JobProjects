#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class UnionFind:
    """
    带size和rank的并查集模板
    """
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.size = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
            self.size[x] = 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.fa[rx] = ry
                self.size[ry] += self.size[rx]
            else:
                self.fa[ry] = rx
                self.size[rx] += self.size[ry]
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] += 1


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 第一次遍历，将所有1和周边1的联通情况，即最初岛屿的情况维护到并查集中
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                uf.find((i, j))
                for a, b in direcs:
                    ni, nj = i + a, j + b
                    if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                    if grid[ni][nj] == 0: continue
                    uf.union((i, j), (ni, nj))

        # 第二次遍历，遍历所有0，并检查将其变为1后的收益
        max_area = max(uf.size.values()) if len(uf.size) > 0 else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: continue
                seen_island = set()    # 这个哈希集用来维护0周边的1所属的联通分量的根节点
                for a, b in direcs:
                    ni, nj = i + a, j + b
                    if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                    if grid[ni][nj] == 0: continue
                    seen_island.add(uf.find((ni, nj)))
                max_area = max(max_area, 1 + sum(uf.size[island] for island in seen_island))

        return max_area

