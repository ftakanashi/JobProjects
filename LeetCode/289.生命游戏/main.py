#!/usr/bin/env python
from typing import List

import itertools
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        status = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for a, b in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    if a == b == 0: continue
                    if i + a < 0 or i + a >= m or j + b < 0 or j + b >=n: continue
                    status[i][j] += board[i+a][j+b]
        # print(status)
        for i in range(m):
            for j in range(n):
                new = board[i][j]
                if status[i][j] < 2: new = 0
                elif status[i][j] == 2: pass
                elif status[i][j] == 3: new = 1
                elif status[i][j] > 3: new = 0
                board[i][j] = new