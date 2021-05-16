#!/usr/bin/env python

from typing import List

import collections

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        nums = list(counter.keys())
        nums.sort()
        dp0, dp1 = 0, counter[nums[0]] * nums[0]
        ans = dp1
        for i in range(1, len(nums)):
            base = 0
            if nums[i-1] < nums[i] - 1: base = dp1
            elif i > 1: base = dp0
            new_dp = max(dp1, base + nums[i] * counter[nums[i]])
            dp0, dp1 = dp1, new_dp
            ans = max(ans, dp1)
        return ans

        # dp = [0 for _ in range(len(nums))]
        # dp[0] = counter[nums[0]] * nums[0]
        # for i in range(1, len(nums)):
        #     base = 0
        #     if nums[i-1] < nums[i] - 1:
        #         base = dp[i-1]
        #     elif i > 1:
        #         base = dp[i-2]
        #     dp[i] = max(dp[i-1], nums[i] * counter[nums[i]] + base)

        # return max(dp)