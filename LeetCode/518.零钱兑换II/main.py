#!/usr/bin/env python

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(1, m+1):
            for j in range(1, amount + 1):
                if j - coins[i-1] >= 0:
                    dp[j] += dp[j - coins[i-1]]
        return dp[-1]

        # dp = [[0 for _ in range(amount + 1)] for _ in range(m + 1)]
        # dp[0][0] = 1
        # for i in range(1, m + 1):
        #     for j in range(amount + 1):
        #         if j == 0:
        #             dp[i][j] = 1
        #         elif j - coins[i-1] >= 0:
        #             dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
        #         else:
        #             dp[i][j] = dp[i-1][j]

        # return dp[-1][-1]