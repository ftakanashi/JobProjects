#!/usr/bin/env python
from typing import List

class Solution1:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        direc = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        def search(x, y):
            cnt = 0
            for a, b in direc:
                nx, ny = x, y
                while 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 'E': cnt += 1
                    elif grid[nx][ny] == 'W': break
                    nx += a
                    ny += b
            return cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '0': continue
                ans = max(ans, search(i, j))
        return ans

class Solution2:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0,0,0,0] for _ in range(n)] for _ in range(m)]

        # 扫描确定向左可以炸掉多少人
        for i in range(m):
            if grid[i][0] == 'E': dp[i][0][0] = 1
            for j in range(1, n):
                if grid[i][j] == 'W': dp[i][j][0] = 0
                elif grid[i][j] == 'E': dp[i][j][0] = dp[i][j-1][0] + 1
                else: dp[i][j][0] = dp[i][j-1][0]
        # 上
        for j in range(n):
            if grid[0][j] == 'E': dp[0][j][1] = 1
            for i in range(1, m):
                if grid[i][j] == 'W': dp[i][j][1] = 0
                elif grid[i][j] == 'E': dp[i][j][1] = dp[i-1][j][1] + 1
                else: dp[i][j][1] = dp[i-1][j][1]
        # 右
        for i in range(m):
            if grid[i][n-1] == 'E': dp[i][n-1][2] = 1
            for j in range(n-2, -1, -1):
                if grid[i][j] == 'W': dp[i][j][2] = 0
                elif grid[i][j] == 'E': dp[i][j][2] = dp[i][j+1][2] + 1
                else: dp[i][j][2] = dp[i][j+1][2]
        # 下
        for j in range(n):
            if grid[m-1][j] == 'E': dp[m-1][j][3] = 1
            for i in range(m-2, -1, -1):
                if grid[i][j] == 'W': dp[i][j][3] = 0
                elif grid[i][j] == 'E': dp[i][j][3] = dp[i+1][j][3] + 1
                else: dp[i][j][3] = dp[i+1][j][3]
        # print(dp)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    ans = max(ans, sum(dp[i][j]))
        return ans