#!/usr/bin/env python
from typing import List

class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1: return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1: return 0
        direc = [(1, 0), (0, 1)]
        mem = [[-1 for _ in range(n)] for _ in range(m)]
        mem[m-1][n-1] = 1

        def dfs(x: int, y: int) -> int:
            if mem[x][y] > 0:
                return mem[x][y]
            count = 0
            for a, b in direc:
                if 0 <= x + a < m and 0 <= y + b < n and obstacleGrid[x+a][y+b] == 0:
                    count += dfs(x + a, y + b)
            mem[x][y] = count
            return count

        dfs(0, 0)
        return mem[0][0]