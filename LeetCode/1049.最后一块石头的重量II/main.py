#!/usr/bin/env python
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        limit = sum(stones) // 2
        m = len(stones)
        dp = [0 for _ in range(limit + 1)]
        for i in range(1, m+1):
            stone = stones[i-1]
            for j in range(limit, 0, -1):
                if j - stone >= 0:
                    dp[j] = max(dp[j], dp[j-stone] + stone)

        return sum(stones) - dp[-1] * 2

        # 非状态压缩版本
        # dp = [[0 for _ in range(limit + 1)] for _ in range(m + 1)]
        # for i in range(1, m+1):
        #     stone = stones[i-1]
        #     for j in range(1, limit+1):
        #         if j - stone >= 0:
        #             dp[i][j] = max(dp[i-1][j], dp[i-1][j-stone] + stone)
        #         else:
        #             dp[i][j] = dp[i-1][j]
        #
        # return sum(stones) - 2 * dp[-1][-1]