#!/usr/bin/env python
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

        # dp = [0 for _ in range(n+1)]
        # for i in range(m):
        #     prev = 0
        #     for j in range(1, n+1):
        #         new_v = prev + 1 if nums1[i] == nums2[j-1] else max(dp[j-1], dp[j])
        #         prev = dp[j]
        #         dp[j] = new_v
        # return dp[-1]