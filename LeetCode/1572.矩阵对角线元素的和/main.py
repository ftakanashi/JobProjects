#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, n = 0, len(mat)
        mid = n // 2
        for i in range(n):
            ans += mat[i][i] + mat[i][n - 1 - i]
        ans -= mat[mid][mid] * (n & 1)
        return ans