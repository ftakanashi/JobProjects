#!/usr/bin/env python

from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def l2t(b):
            return tuple([tuple(row) for row in b])

        def t2l(b):
            return [list(row) for row in b]

        def find_zero(b):
            for i in range(2):
                for j in range(3):
                    if b[i][j] == 0: return (i, j)

        target = ((1,2,3), (4,5,0))
        queue = deque()
        queue.append((l2t(board), 0))
        seen = set()
        while queue:
            status, times = queue.popleft()
            if status == target: return times
            if status in seen: continue
            seen.add(status)
            x, y = find_zero(status)
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+a, y+b
                if nx < 0 or nx > 1 or ny < 0 or ny > 2: continue
                list_status = t2l(status)
                tmp = list_status[nx][ny]
                list_status[nx][ny] = 0
                list_status[x][y] = tmp
                new_status = l2t(list_status)
                queue.append((new_status, times + 1))

        return -1