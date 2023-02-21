#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import deque

class HashQueue:
    """
    一个自带seen哈希集的辅助队列类
    这里特别适配此题，采用 val[:3] 作为哈希集的key
    """
    def __init__(self):
        self.q = deque()
        self.seen = set()

    def popleft(self):
        return self.q.popleft()

    def append(self, val):
        if val[:3] in self.seen:
            return
        self.q.append(val)
        self.seen.add(val[:3])

    def __len__(self):
        return len(self.q)


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = HashQueue()
        queue.append((0, 0, 0, 0))
        while len(queue) > 0:
            x, y, status, step = queue.popleft()
            if x == m - 1 and y == n - 2:
                return step

            # 将说明中的BFS规则转化为代码即可
            if status == 0:
                if y + 2 < n and grid[x][y + 2] == 0:
                    queue.append((x, y + 1, 0, step + 1))
                if x < m - 1 and grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                    queue.append((x + 1, y, 0, step + 1))
                    queue.append((x, y, 1, step + 1))
            else:
                if x + 2 < m and grid[x + 2][y] == 0:
                    queue.append((x + 1, y, 1, step + 1))
                if y < n - 1 and grid[x][y + 1] == grid[x + 1][y + 1] == 0:
                    queue.append((x, y + 1, 1, step + 1))
                    queue.append((x, y, 0, step + 1))

        return -1