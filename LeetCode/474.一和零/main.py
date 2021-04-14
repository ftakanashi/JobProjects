#!/usr/bin/env python
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ones, zeros = [], []
        for s in strs:
            ones.append(s.count('1'))
            zeros.append(s.count('0'))

        # dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        # for i in range(1, len(strs) + 1):
        #     for j in range(m + 1):
        #         for k in range(n + 1):
        #             if j - zeros[i - 1] >= 0 and k - ones[i - 1] >= 0:
        #                 dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros[i-1]][k-ones[i-1]] + 1)
        #             else:
        #                 dp[i][j][k] = dp[i-1][j][k]
        # print(dp)
        # return dp[-1][-1][-1]

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, len(strs)+1):
            c_0, c_1 = zeros[i-1], ones[i-1]
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j - c_0 >= 0 and k - c_1 >= 0:
                        dp[j][k] = max(dp[j][k], dp[j-c_0][k-c_1] + 1)

        return dp[-1][-1]

