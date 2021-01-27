#!/usr/bin/env python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        n = len(nums)
        yes, no = nums[0], 0
        for i in range(1, n):
            tmp = yes
            yes = no + nums[i]
            no = max(tmp, no)
        return max(yes, no)

        # 非状态压缩版
        # dp = [[0,0] for _ in range(n)]
        # dp[0] = [nums[0], 0]
        # for i in range(1, n):
            # dp[i][0] = dp[i-1][1] + nums[i]
            # dp[i][1] = max(dp[i-1])
        # return max(dp[-1])