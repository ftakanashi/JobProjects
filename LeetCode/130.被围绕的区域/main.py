#!/usr/bin/env python
from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if (0 < i < m-1 and 0 < j < n-1) or board[i][j] == 'X': continue
                # 只对边缘的O格子开始扫描

                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    if board[x][y] == 'T': continue
                    board[x][y] = 'T'
                    for a, b in direcs:
                        nx, ny = x+a, y+b
                        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                            queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == 'T': board[i][j] = 'O'