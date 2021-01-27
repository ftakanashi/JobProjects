#!/usr/bin/env python
from typing import List

import collections
class UnionFind:
    def __init__(self):
        self.fa = {}
        self.name_map = {}

    def find(self, x, name=None):
        if x not in self.fa:
            self.fa[x] = x
            self.name_map[x] = name
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_y] = root_x
            self.name_map[root_y] = self.name_map[root_x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        for info in accounts:
            i = 1
            uf.find(info[1], name=info[0])
            while i < len(info) - 1:
                uf.union(info[i], info[i+1])
                i += 1
        final_res = []
        res = collections.defaultdict(list)
        for k in uf.fa:
            root = uf.find(k)
            res[root].append(k)
        for k, accs in res.items():
            tmp = [uf.name_map[k],]
            tmp.extend(list(sorted(accs)))
            final_res.append(tmp)

        return final_res