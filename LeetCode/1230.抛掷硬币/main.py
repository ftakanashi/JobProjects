#!/usr/bin/env python
from typing import List

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        m = len(prob)
        dp = [[0 for _ in range(target + 1)] for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m+1):
            p = prob[i-1]
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j] * (1 - p)
                if j > 0:
                    dp[i][j] += dp[i-1][j-1] * p
        return dp[-1][-1]