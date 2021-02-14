#!/usr/bin/env python
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp [0] = 0
        for c in coins:
            if c < len(dp): dp[c] = 1

        for i in range(1, amount + 1):
            for c in coins:
                if i - c > 0: dp[i] = min(dp[i], dp[i-c] + 1)

        return dp[amount] if dp[amount] < float('inf') else -1