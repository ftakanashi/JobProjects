#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])

        for key in d:
            d[key].sort()
            if key >= 0:
                i, j = key, 0
            else:
                i, j = 0, -key
            for num in d[key]:
                mat[i][j] = num
                i += 1
                j += 1

        return mat