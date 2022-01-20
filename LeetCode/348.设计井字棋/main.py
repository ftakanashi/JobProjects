#!/usr/bin/env python
from collections import Counter

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [Counter() for _ in range(n)]
        self.cols = [Counter() for _ in range(n)]
        self.slash = Counter()
        self.revslash = Counter()

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        self.rows[row][player] += 1
        if self.rows[row][player] == n: return player
        self.cols[col][player] += 1
        if self.cols[col][player] == n: return player
        if row == col:
            self.slash[player] += 1
            if self.slash[player] == n: return player
        if row + col == n - 1:
            self.revslash[player] += 1
            if self.revslash[player] == n: return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)