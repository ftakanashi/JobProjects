#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def movingCount(self, m: int, n: int, k: int) -> int:
        checked = [[0 for _ in range(n)] for _ in range(m)]
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def sum_digit(x: int, y: int):
            '''
            判断某个坐标的格子是不是障碍物（不能走通的那种
            '''
            xa, xb = x // 10, x % 10
            ya, yb = y // 10, y % 10
            return xa + xb + ya + yb

        def dfs(x: int, y: int):
            if sum_digit(x, y) > k:
                return

            checked[x][y] = 1
            for a, b in direc:
                if 0 <= x + a < m and 0 <= y + b < n and checked[x+a][y+b] == 0:
                    dfs(x+a, y+b)

        dfs(0, 0)
        return sum([sum(row) for row in checked])