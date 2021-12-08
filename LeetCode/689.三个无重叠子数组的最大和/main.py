#!/usr/bin/env python
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # 构建DP数组以及path
        dp = [[0 for _ in range(n+1)] for _ in range(4)]
        path = [[list() for _ in range(n+1)] for _ in range(4)]

        # 构建前缀和数组
        s, presum = 0, [0, ]
        for num in nums:
            s += num
            presum.append(s)

        # 类背包问题递推
        for i in range(1, 4):
            for j in range(1, n+1):
                if j < i * k: continue    # 当j小于i*k时必然无法凑齐i个长度为k的子数组，因此直接跳过

                # 取用 nums[j] 的情况
                take = dp[i-1][j-k] + presum[j] - presum[j-k]
                # 由于DP数组的列宽度恰好和presum数组的长度一样，刚好是n+1，所以这里可以直接presum[j] - presum[j-k]

                # 不取用 nums[j] 的情况
                not_take = dp[i][j-1]

                if not_take >= take:
                    dp[i][j] = not_take
                    path[i][j] = path[i][j-1]
                else:
                    dp[i][j] = take
                    path[i][j] = path[i-1][j-k] + [j-k, ]

        return path[-1][-1]