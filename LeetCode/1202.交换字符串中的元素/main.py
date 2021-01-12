#!/usr/bin/env python
from typing import List

import collections

class UnionFind:
    def __init__(self, n, cons):
        self.fa = [i for i in range(n)]
        # 初始化完成后顺便把合并操作一并做掉
        for a, b in cons:
            self.union(a, b)
        for i in range(n):    # 这是为了处理那个bug(见并查集README
            self.find(i)

    def find(self, x):
        r = x
        while r != self.fa[r]:
            r = self.fa[r]

        while x != self.fa[x]:
            tmp = self.fa[x]
            self.fa[x] = r
            x = tmp
        return r

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_y] = root_x

    def fa_to_dict(self):
        # 将合并完成后的并查集的fa转换为一个按分量分开的dict，方便后续处理
        res = collections.defaultdict(list)
        for i, f in enumerate(self.fa):
            res[f].append(i)
        return res

class Solution1:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n, pairs)
        fa_dict = uf.fa_to_dict()
        res = [None for _ in range(n)]
        for k, chars in fa_dict.items():
            for i, ch in enumerate(sorted([s[ci] for ci in chars])):
                res[chars[i]] = ch
        return ''.join(res)