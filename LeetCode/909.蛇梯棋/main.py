#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def num2xy(num):
            row = (num-1) // n
            x = n - 1 - row
            rev = (row & 1 == 1)
            if rev:
                y = n - 1 - ((num-1) % n)
            else:
                y = (num-1) % n
            return x, y

        queue = deque()
        queue.append((1, 0))
        seen = set()
        while queue:
            num, times = queue.popleft()
            if num == n*n: return times
            if num in seen: continue
            seen.add(num)
            for i in range(1, 7):
                if num + i > n*n: break
                x, y = num2xy(num + i)
                if board[x][y] != -1:
                    queue.append((board[x][y], times + 1))
                else:
                    queue.append((num + i, times + 1))
        return -1