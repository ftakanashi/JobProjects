#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = matrix[0].copy()
        F = float("inf")

        for i in range(1, m):
            new_dp = [0 for _ in range(n)]
            for j in range(n):
                cands = [dp[j], dp[j - 1] if j > 0 else F, dp[j + 1] if j < n - 1 else F]
                new_dp[j] = min(cands) + matrix[i][j]
            dp = new_dp

        return min(dp)

        # dp = [[F for _ in range(n)] for _ in range(m)]
        # for j in range(n):
        #     dp[0][j] = matrix[0][j]
        #
        # for i in range(1, m):
        #     for j in range(n):
        #         if j - 1 >= 0:
        #             dp[i][j] = min(dp[i-1][j-1] + matrix[i][j], dp[i][j])
        #         if j + 1 < n:
        #             dp[i][j] = min(dp[i-1][j+1] + matrix[i][j], dp[i][j])
        #         dp[i][j] = min(dp[i-1][j] + matrix[i][j], dp[i][j])
        #
        # return min(dp[-1])