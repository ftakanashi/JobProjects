#!/usr/bin/env python
from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        def str_max(a, b):
            if a is None: return b
            if b is None: return a
            if len(a) > len(b): return a
            if len(a) < len(b): return b
            return max(a, b)

        dp = ['' for _ in range(target + 1)]
        for i in range(1, 10):
            c, ch = cost[i-1], str(i)
            for j in range(1, target + 1):
                if (j-c > 0 and dp[j-c]) or j-c == 0:
                    dp[j] = str_max(dp[j], ch + dp[j-c])
        return dp[-1] if dp[-1] else '0'

        # dp = [[None for _ in range(target + 1)] for _ in range(10)]
        # for i in range(10): dp[i][0] = ''
        # for i in range(1, 10):
        #     c = cost[i-1]
        #     ch = str(i)
        #     for j in range(1, target+1):
        #         if j - c >= 0 and dp[i][j-c] is not None:
        #             dp[i][j] = str_max(dp[i-1][j], ch + dp[i][j-c])
        #         else:
        #             dp[i][j] = dp[i-1][j]

        # return dp[-1][-1] if dp[-1][-1] else '0'