#!/usr/bin/env python
from functools import lru_cache as cache

class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        direcs = [(0,1),(0,-1),(1,0),(-1,0)]

        @cache
        def dfs(x, y, moves):
            if moves > maxMove:
                return 0
            elif x < 0 or x >= m or y < 0 or y >= n:
                return 1

            cnt = 0
            for a, b in direcs:
                nx, ny = x+a, y+b
                cnt = (dfs(nx, ny, moves + 1) + cnt) % (10**9 + 7)
            return cnt

        return dfs(startRow, startColumn, 0)

class Solution2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0: return 0

        dp = [[[0 for _ in range(maxMove)] for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn][0] = 1
        direcs = [(0,1),(0,-1),(1,0),(-1,0)]
        for t in range(1, maxMove):
            for i in range(m):
                for j in range(n):
                    for a, b in direcs:
                        ni, nj = i+a, j+b
                        if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                        dp[i][j][t] += dp[ni][nj][t-1]

        ans = 0
        for i in range(m):
            ans += sum(dp[i][0])
            ans += sum(dp[i][-1])
        for j in range(n):
            ans += sum(dp[0][j])
            ans += sum(dp[-1][j])
        return ans % (10**9+7)