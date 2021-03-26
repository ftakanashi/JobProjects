#!/usr/bin/env python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        if n < 2 or s & 1 == 1: return False
        target = s // 2

        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if dp[i-1][j]: dp[i][j] = True
                elif j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j - nums[i-1]]
        return dp[-1][-1]