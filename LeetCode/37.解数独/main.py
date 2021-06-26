#!/usr/bin/env python
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def update(x, y, n):
            if type(n) is str: n = int(n)
            k = (x // 3) * 3 + (y // 3)
            rows[x] |= (1 << (n-1))
            cols[y] |= (1 << (n-1))
            cells[k] |= (1 << (n-1))

        def remove(x, y, n):
            if type(n) is str: n = int(n)
            k = (x // 3) * 3 + (y // 3)
            rows[x] ^= (1 << (n-1))
            cols[y] ^= (1 << (n-1))
            cells[k] ^= (1 << (n-1))

        def check(x, y, n):
            if rows[x] & (1 << (n-1)) > 0: return False
            if cols[y] & (1 << (n-1)) > 0: return False
            k = (x // 3) * 3 + (y // 3)
            if cells[k] & (1 << (n-1)) > 0: return False
            return True

        rows = [0 for _ in range(9)]
        cols = [0 for _ in range(9)]
        cells = [0 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                update(i, j, board[i][j])

        def dfs(x, y):
            if x == 9: return True
            if board[x][y] == '.':
                for n in range(1, 10):
                    if check(x, y, n):
                        board[x][y] = str(n)
                        update(x, y, n)
                        flag = dfs(x+1, 0) if y == 8 else dfs(x, y+1)
                        if flag: return True
                        remove(x, y, n)
                board[x][y] = '.'
            else:
                flag = dfs(x+1, 0) if y == 8 else dfs(x, y+1)
                if flag: return True

            return False

        dfs(0, 0)