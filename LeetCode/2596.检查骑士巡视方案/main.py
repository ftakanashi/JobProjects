#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0: return False
        n = len(grid)
        opts = [-2, -1, 1, 2]
        pos_map = {}
        for i in range(n):
            for j in range(n):
                pos_map[grid[i][j]] = (i, j)

        curr = 0
        while curr + 1 < n * n:
            curr_x, curr_y = pos_map[curr]
            nxt_x, nxt_y = pos_map[curr + 1]
            dx, dy = nxt_x - curr_x, nxt_y - curr_y
            if dx in opts and dy in opts and abs(dx) != abs(dy):    # 判断是否符合骑士走步的规则
                curr += 1
            else:
                return False

        return True