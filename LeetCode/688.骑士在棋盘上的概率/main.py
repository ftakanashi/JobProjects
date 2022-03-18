#!/usr/bin/env python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        direcs = [
            (-1, -2), (-2, -1), (-2, 1), (-1, 2),
            (1, -2), (2, -1), (1, 2), (2, 1)
        ]

        @cache
        def dfs(rest, pos):
            x, y = pos
            if x < 0 or x >= n or y < 0 or y >= n: return 0.0
            if rest == 0: return 1.0
            total = 0.0
            for a, b in direcs:
                nx, ny = x+a, y+b
                total += dfs(rest-1, (nx, ny))
            return total / 8

        return dfs(k, (row, column))