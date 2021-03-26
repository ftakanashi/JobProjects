#!/usr/bin/env python
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        self.mem = [[0 for _ in range(n)] for _ in range(m)]

        s = 0
        for j in range(n):
            s += matrix[0][j]
            self.mem[0][j] = s

        s = 0
        for i in range(m):
            s += matrix[i][0]
            self.mem[i][0] = s

        for i in range(1, m):
            for j in range(1, n):
                self.mem[i][j] = self.mem[i][j-1] + self.mem[i-1][j] - self.mem[i-1][j-1] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        base = self.mem[row2][col2]
        if col1 > 0:
            base -= self.mem[row2][col1-1]
        if row1 > 0:
            base -= self.mem[row1-1][col2]
        if row1 > 0 and col1 > 0:
            base += self.mem[row1-1][col1-1]
        return base

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)