#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class UnionFind(object):
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        r = x
        while r != self.fa[r]:
            r = self.fa[r]
        while x != r:
            tmp = self.fa[x]
            self.fa[x] = r
            x = tmp
        return r

    def union(self, x, y):
        if x == y: return False
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_x] = root_y  # 每实际发生一次集合的合并，才会导致连通分量数减少
            # 所以只有union返回True才让外部的count减去1。
            return True
        return False

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)
        count = n
        for i in range(n):
            for j in range(i + 1):
                if M[i][j] == 1 and uf.union(i, j):
                    count -= 1
        return count