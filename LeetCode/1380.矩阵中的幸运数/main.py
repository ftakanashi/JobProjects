#!/usr/bin/env python

from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min = [float('inf') for _ in range(m)]
        col_max = [float('-inf') for _ in range(n)]
        for i in range(m):
            for j in range(n):
                row_min[i] = min(row_min[i], matrix[i][j])
                col_max[j] = max(col_max[j], matrix[i][j])

        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row_min[i] == col_max[j]:
                    ans.append(matrix[i][j])
        return ans