#!/usr/bin/env python
from typing import List

class UnionFind:    # 带实时统计连通分量个数功能的并查集
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.cnt = 0

    def getCount(self):
        return self.cnt

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.cnt -= 1
            if self.rank[root_x] < self.rank[root_y]:
                self.fa[root_x] = root_y
            else:
                self.fa[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
            self.cnt += 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        lands = set()
        uf = UnionFind()
        direcs = [(0,1),(0,-1),(1,0),(-1,0)]

        for x, y in positions:
            num = x * n + y
            uf.find(num)    # 别忘了这一步，相当于是把这个点加入到并查集中，但是并未做任何union

            for a, b in direcs:
                nx, ny = x+a, y+b
                nnum = nx * n + ny
                if (nx, ny) in lands:
                    uf.union(num, nnum)

            ans.append(uf.getCount())
            lands.add((x, y))
        return ans