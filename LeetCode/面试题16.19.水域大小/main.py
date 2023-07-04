#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import itertools
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        direcs = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
        seen = set()

        def dfs(x, y):
            seen.add((x, y))
            tmp = 0
            for a, b in direcs:
                if a == b == 0: continue
                nx, ny = x + a, y + b
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if land[nx][ny] != 0: continue
                if (nx, ny) in seen: continue
                tmp += dfs(nx, ny)
            return tmp + 1

        ponds = []
        for i in range(m):
            for j in range(n):
                if land[i][j] != 0: continue
                if (i, j) in seen: continue
                ponds.append(dfs(i, j))

        ponds.sort()
        return ponds