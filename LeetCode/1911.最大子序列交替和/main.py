#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = nums[0], 0
        for i in range(1, n):
            new_a = max(a, b + nums[i])
            new_b = max(b, a - nums[i])
            a, b = new_a, new_b
        return a

        # 无状态压缩优化的情况：
        # dp = [[0, 0] for _ in range(n)]
        # dp[0][0] = nums[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - nums[i])
        # return dp[-1][0]