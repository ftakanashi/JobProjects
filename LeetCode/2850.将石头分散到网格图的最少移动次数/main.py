#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 构建more和less数组
        more, less = [], []
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1: more.extend([(i, j)] * (grid[i][j] - 1))
                elif grid[i][j] == 0: less.append((i, j))

        # 获取more的全排列
        n = len(more)
        perms = []
        def dfs(pos):
            if pos == n - 1:
                perms.append(more.copy())
                return
            seen = set()
            for i in range(pos, n):
                if more[i] in seen: continue
                seen.add(more[i])
                more[pos], more[i] = more[i], more[pos]
                dfs(pos + 1)
                more[pos], more[i] = more[i], more[pos]

        dfs(0)

        # 根据全排列中每个排列与less的对应，形成一种方案，统计该方案中的移动次数，并计算全局最小值
        ans = float("inf")
        for perm in perms:
            steps = 0
            for (mx, my), (lx, ly) in zip(perm, less):
                steps += abs(mx - lx) + abs(my - ly)
            ans = min(ans, steps)
        return ans