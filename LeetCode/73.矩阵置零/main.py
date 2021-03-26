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

class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for j in range(n):
            if matrix[0][j] == 0: first_row_has_zero = True
        for i in range(m):
            if matrix[i][0] == 0: first_col_has_zero = True

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n): matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(m): matrix[i][0] = 0

class Solution2_mod:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = first_col_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0 or j == 0:
                        first_row_zero = first_row_zero or i == 0
                        first_col_zero = first_col_zero or j == 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0

        if first_row_zero: matrix[0] = [0 for _ in range(n)]
        if first_col_zero:
            for i in range(m): matrix[i][0] = 0