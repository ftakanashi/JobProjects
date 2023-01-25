#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        fa = [i for i in range(n)]

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(x, y):
            fa[find(x)] = fa[find(y)]

        for a, b in edges:
            merge(a, b)

        return find(source) == find(destination)