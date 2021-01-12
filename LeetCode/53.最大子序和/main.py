#!/usr/bin/nev python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        prev_s = max_s = nums[0]
        for i in range(1, n):
            s = max(prev_s + nums[i], nums[i])
            if s > max_s:
                max_s = s
            prev_s = s
        return max_s

        # 无状态压缩版本
        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        #
        # return max(dp)