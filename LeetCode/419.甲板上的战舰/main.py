#!/usr/bin/env python

from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and \
                        (i == 0 or board[i-1][j] == '.') and \
                        (j == 0 or board[i][j-1] == '.'):
                    ans += 1
        return ans