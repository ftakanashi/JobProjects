#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.count = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0
            self.count[x] = 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return
        if self.rank[root_x] < self.rank[root_y]:
            self.fa[root_x] = root_y
            self.count[root_y] += self.count[root_x]
        else:
            self.fa[root_y] = root_x
            self.count[root_x] += self.count[root_y]
            if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        uf = UnionFind()
        for num in nums:
            uf.find(num)
            if num - 1 in nums_set: uf.union(num - 1, num)
            if num + 1 in nums_set: uf.union(num, num + 1)
        return max(uf.count.values()) if uf.count.values() else 0