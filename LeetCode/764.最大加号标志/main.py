#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = {(a, b) for a, b in mines}
        if n == 1: return 1 if len(mines) == 0 else 0

        dp = [
            [[0 if (i, j) in mines else 1] * 4 for j in range(n)]
            for i in range(n)
        ]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if (i, j) in mines: continue
                if (i, j - 1) not in mines:
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                if (i - 1, j) not in mines:
                    dp[i][j][1] = dp[i - 1][j][1] + 1

        for i in range(n - 2, 0, -1):
            for j in range(n - 2, 0, -1):
                if (i, j) in mines: continue
                if (i, j + 1) not in mines:
                    dp[i][j][2] = dp[i][j + 1][2] + 1
                if (i + 1, j) not in mines:
                    dp[i][j][3] = dp[i + 1][j][3] + 1

        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, min(dp[i][j]))
        return ans