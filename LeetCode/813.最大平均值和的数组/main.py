#!/usr/bin/env python
from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        presum = [0, ]
        for num in nums: presum.append(presum[-1] + num)

        n = len(nums)
        dp = [[0 for _ in range(k)] for _ in range(n)]
        for i in range(n): dp[i][0] = presum[i+1] / (i+1)

        for i in range(n):
            for j in range(1, k):
                if j > i: break
                for x in range(i):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[x][j-1] + (presum[i+1] - presum[x+1]) / (i - x)
                    )

        return dp[-1][-1]