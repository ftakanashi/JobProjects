#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter

class UnionFind:
    """
    标准并查集模板
    """
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0  # 初始化
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:  # 这里加上判断
                self.fa[root_x] = root_y  # x的rank至少比y的rank-1小，因此即使合并过去self.rank[root_y]不会变
            else:
                self.fa[root_y] = root_x
                # 别忘了相等时及时加深度
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        for i, j in edges: uf.union(i, j)
        mapping = Counter()
        for i in range(n):
            root = uf.find(i)
            mapping[root] += 1

        ans = 0
        for v in mapping.values():
            ans += (v * (n - v))
        return ans // 2