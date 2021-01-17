#!/usr/bin/env python
from typing import List

class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rowi = set([])
        zero_coli = set([])
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rowi.add(i)
                    zero_coli.add(j)

        for row in zero_rowi:
            matrix[row] = [0 for _ in range(n)]

        for i in range(m):
            for j in zero_coli:
                matrix[i][j] = 0

