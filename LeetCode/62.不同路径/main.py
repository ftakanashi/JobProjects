#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = [1 for _ in range(n)]

        for i in range(m - 1):
            for j in range(1, n):
                steps[j] = steps[j - 1] + steps[j]

        return steps[-1]

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        path_map = [[-1 for _ in range(n)] for _ in range(m)]
        direc = [(1, 0), (0, 1)]

        def dfs(x: int, y: int) -> int:
            if x == m - 1 and y == n - 1:
                return 1
            count = 0
            for a, b in direc:
                if x + a >= m or y + b >= n:
                    continue
                if path_map[x+a][y+b] < 0:
                    path_map[x+a][y+b] = dfs(x+a, y+b)
                count += path_map[x+a][y+b]

            return count

        return dfs(0, 0)