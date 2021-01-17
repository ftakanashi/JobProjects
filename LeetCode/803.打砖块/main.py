#!/usr/bin/env python

from typing import List

import copy
class UnionFind:
    '''
    带有"以某个节点为根节点的 节点数量统计 功能的并查集实现
    '''
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.fa[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def getSize(self, x):
        return self.size[self.find(x)]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])

        def p2v(x1, x2):
            return x1 * n + x2

        grid_copy = copy.deepcopy(grid)    # 做副本
        # 将所有会被打碎的砖块打碎
        for hit in hits:
            h1, h2 = hit
            grid_copy[h1][h2] = 0

        uf = UnionFind(m * n + 1)
        roof_i = m * n    # 虚拟屋顶
        for j in range(n):
            if grid_copy[0][j] == 1: uf.union(j, roof_i)    # 第一行所有砖块和虚拟屋顶相连

        # 将剩余砖块（即使在会被打碎砖块全被打碎后）仍然和屋顶可连通的节点入并查集
        for i in range(1, m):
            for j in range(n):
                if grid_copy[i][j] == 0: continue
                if grid_copy[i - 1][j] == 1:
                    uf.union(p2v(i-1, j), p2v(i, j))
                if j > 0 and grid_copy[i][j - 1] == 1:
                    uf.union(p2v(i, j-1), p2v(i, j))

        # 逆序遍历hits
        res = [0 for _ in range(len(hits))]
        for i in range(len(hits) - 1, -1, -1):
            hit = hits[i]
            h1, h2 = hit
            if grid[h1][h2] == 0: continue    # 若这个地方在原先的图里就是空的，相当于打碎一个空砖块。没有不会发生砖块掉落
            origin = uf.getSize(roof_i)    # 执行补回操作前与屋顶想通的砖块数

            # 如果补回的砖块是第一行的，则直接将其与屋顶相连
            if h1 == 0:
                uf.union(p2v(h1, h2), roof_i)
            for d1, d2 in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                if 0 <= h1 + d1 < m and 0 <= h2 + d2 < n and grid_copy[h1+d1][h2+d2] == 1:
                    uf.union(p2v(h1+d1, h2+d2), p2v(h1, h2))

            current = uf.getSize(roof_i)    # 执行补回操作后与屋顶相通的砖块数
            # 某些特别情况下，虽然当前的hit在原图中确实是1，但是其实他是在更早的hit过程中因为失去屋顶连接而自动掉落的
            # 此时current - origin - 1会是负数。但是实际上他不在这步脱落，因此应该是0。所以加上max函数进行修正
            res[i] = max(0, current - origin - 1)

            grid_copy[h1][h2] = 1

        return res