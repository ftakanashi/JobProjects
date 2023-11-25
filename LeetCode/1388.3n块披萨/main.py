#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def runDP(self, nums: List[int]) -> int:
        """
        单次DP过程
        """
        m = len(nums)
        n = (m + 1) // 3    # 注意这个+1，相当于是还原原slices的长度

        dp = [[0 for _ in range(n + 1)] for _ in range(m)]
        dp[0][1] = nums[0]
        dp[1][1] = max(nums[0], nums[1])
        for j in range(2, n + 1):
            dp[0][j] = dp[1][j] = float("-inf")

        for i in range(2, m):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 2][j - 1] + nums[i], dp[i - 1][j])

        return max(dp[-1])

    def maxSizeSlices(self, slices: List[int]) -> int:
        # 取两者较大值
        return max(self.runDP(slices[1:]), self.runDP(slices[:-1]))