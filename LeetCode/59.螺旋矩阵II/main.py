#!/usr/bin/env python
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        direcs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(i: int, j: int, di: int, num: int) -> bool:
            if i < 0 or i >= n or j < 0 or j >= n or matrix[i][j] is not None:
                return False
            matrix[i][j] = num
            a, b = direcs[di]
            if not dfs(i+a, j+b, di, num+1):
                di = 0 if di >= 3 else di + 1
                a, b = direcs[di]
                dfs(i+a, j+b, di, num+1)
            return True

        dfs(0, 0, 0, 1)
        return matrix