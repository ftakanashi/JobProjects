#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [arr[0], 0]
        ans = arr[0]
        for i in range(1, len(arr)):
            num = arr[i]
            new_dp = [0, 0]
            new_dp[0] = max(dp[0] + num, num)
            new_dp[1] = max(dp[0], dp[1] + num)
            ans = max(ans, max(new_dp))
            dp = new_dp

        # 不压缩状态的情况
        # dp = [[0, 0] for _ in range(len(arr))]
        # dp[0][0] = ans = arr[0]
        # for i in range(1, len(arr)):
        #     num = arr[i]
        #     dp[i][0] = max(dp[i-1][0] + num, num)
        #     dp[i][1] = max(dp[i-1][0], dp[i-1][1] + num)
        #     ans = max(ans, max(dp[i]))

        return ans