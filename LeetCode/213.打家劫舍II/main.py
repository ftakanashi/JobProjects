#!/usr/bin/env python

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        def do_dp(start: int, end: int):
            n = end - start + 1
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = nums[start]
            for i in range(start + 1, end + 1):
                dp[i-start][0] = max(dp[i-start-1])
                dp[i-start][1] = dp[i-start-1][0] + nums[i]
            return max(dp[-1])

        return max(do_dp(0, len(nums) - 2), do_dp(1, len(nums) - 1))