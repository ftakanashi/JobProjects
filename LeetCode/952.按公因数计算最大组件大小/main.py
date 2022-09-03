#!/usr/bin/env python
from typing import List

import math
from collections import Counter

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.fa[root_x] = root_y
            else:
                self.fa[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind()
        for num in nums:
            i = 2
            while i <= math.sqrt(num):
                if num % i == 0:
                    uf.union(num, i)
                    uf.union(num, num // i)
                i += 1

        return max(Counter([uf.find(num) for num in nums]).values())