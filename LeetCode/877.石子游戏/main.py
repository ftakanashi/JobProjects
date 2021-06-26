#!/usr/bin/env python
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # n = len(piles)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n): dp[i][i] = piles[i]
        #
        # for l in range(1, n):
        #     for i in range(n - l):
        #         j = i + l
        #         dp[i][j] = max(piles[j] - dp[i][j-1], piles[i] - dp[i+1][j])
        #
        # return dp[0][-1] >= 0
        return True