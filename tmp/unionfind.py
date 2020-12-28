#!/usr/bin/env python
# -*- coding:utf-8 -*-

class UnionFind(object):
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        r = x
        while r != self.fa[r]:
            r = self.fa[r]
        while x != self.fa[x]:
            tmp = self.fa[x]
            self.fa[x] = r
            x = tmp
        return x

    def union(self, x, y):
        if x == y: return
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_x] = root_y

    def count(self):
        for i in range(n):
            self.find(i)
        print(self.fa)
        return len(list(set(self.fa)))

if __name__ == '__main__':
    n = 4
    M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1):
            if M[i][j] == 1:
                uf.union(i, j)
    uf.count()