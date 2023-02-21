#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(16)] for _ in range(6)]
        for j in range(6):
            dp[j][1] = 1

        for i in range(n - 1):
            new_dp = [[0 for _ in range(16)] for _ in range(6)]

            for p in range(6):
                for j in range(6):

                    if p == j:
                        for k in range(1, 16):
                            if k < rollMax[j]:
                                new_dp[p][k + 1] += dp[j][k] % mod
                            else:
                                break
                    else:
                        for k in range(1, 16):
                            new_dp[p][1] += dp[j][k] % mod

            dp = new_dp

        ans = 0
        for j in range(6):
            for k in range(1, 16):
                ans = (ans + dp[j][k]) % mod

        return ans