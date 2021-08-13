#!/usr/bin/env python

'''
    通用记忆模板见README.md
'''

class UnionFind:
    '''
    一种比较通用且好记忆的实现
    '''
    def __init__(self):
        self.fa = {}

    def find(self, x: int) -> int:
        if x not in self.fa:
            self.fa[x] = x
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.fa[root_x] = root_y

    def flush(self):
        for i in self.fa:
            self.find(i)

class UnionFind2:
    '''
    带有"以某个节点为根节点的 节点数量统计 功能的并查集实现
    '''
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.size = [1 for _ in range(n)]    # size初始化全是1

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.fa[root_x] = root_y
            self.size[root_y] += self.size[root_x]    # 只有在合并的时候，size会发生变化，相应维护即可

    def getSize(self, x):
        return self.size[self.find(x)]