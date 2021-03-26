#!/usr/bin/env python
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            n = len(nums)
            dp = [1 for _ in range(n)]
            for i in range(n):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)

        return lis([e[1] for e in envelopes])