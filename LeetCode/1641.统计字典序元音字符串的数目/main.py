#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1 for _ in range(5)]

        for i in range(1, n):
            new_dp = dp.copy()

            tmp = 0
            for j in range(5):
                tmp += dp[j]
                new_dp[j] = tmp

            dp = new_dp    # 状态压缩，用 new_dp 替换老 dp

        return sum(dp)