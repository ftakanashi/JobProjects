#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {-1: -1}    # 初始化时直接设置好边界虚拟节点
        self.rank = {-1: float("inf")}    # rank设置为无穷大，这主要是为了后面第二次扫描方便

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.fa[rx] = ry
            else:
                self.fa[ry] = rx
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] += 1

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind()
        f = lambda x, y: x * n + y    # 二维转一维下标
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                ind = f(i, j)
                uf.find(ind)    # 别忘了这一步，因为地图中可能有些陆地格子四周都是0，这里调用一下是为了在uf.fa中占个位
                for a, b in direcs:
                    ni, nj = i+a, j+b
                    nind = f(ni, nj)
                    if 0 <= ni < m and 0 <= nj < n:    # 新格子在地图范围内
                        if grid[ni][nj] == 0: continue
                        uf.union(ind, nind)    # 合并联通分量
                    else:
                        uf.union(ind, -1)    # 新格子在地图范围外，换言之，当前格子(i, j)在边界上，将其与虚拟节点合并

        ans = 0
        for p in uf.fa:
            if uf.find(p) != -1:    # 寻找非边界节点的格子。最上面初始化时-1的rank设置为无穷大，就是为了这里不等号右边可以不写uf.find(-1)
                ans += 1
        return ans