#!/usr/bin/env python
from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        counter = {'X': 0, 'O': 0}    # 棋子计数器
        for row in board:
            for ch in row:
                if ch == ' ': continue
                counter[ch] += 1

        res = {'O': 0, 'X': 0, ' ': 0}    # 成行数计数器，为避免不必要的讨论，将空格也作为元素计入
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]: res[board[i][0]] += 1
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]: res[board[0][j]] += 1
        if board[0][0] == board[1][1] == board[2][2]: res[board[0][0]] += 1
        if board[0][2] == board[1][1] == board[2][0]: res[board[0][2]] += 1

        if counter['X'] == counter['O']: return res['X'] == 0
        elif counter['X'] == counter['O'] + 1: return res['O'] == 0
        return False