#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        val2pos = {}
        for i in range(m):
            for j in range(n):
                val2pos[mat[i][j]] = (i, j)

        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for i, val in enumerate(arr):
            x, y = val2pos[val]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m:
                return i
        return -1