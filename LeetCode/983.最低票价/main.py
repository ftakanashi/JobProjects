#!/usr/bin/env python
from typing import List

from functools import lru_cache as cache
class Solution1:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)

        @cache
        def dfs(day):
            if day > days[-1]: return 0

            if day not in days_set:
                return dfs(day + 1)

            return min(
                dfs(day + 1) + costs[0],
                dfs(day + 7) + costs[1],
                dfs(day + 30) + costs[2]
            )

        return dfs(1)


class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        dp = [0 for _ in range(396)]

        for day in range(days[-1], -1, -1):
            if day not in days_set:
                dp[day] = dp[day + 1]
            else:
                dp[day] = min(
                    dp[day + 1] + costs[0],
                    dp[day + 7] + costs[1],
                    dp[day + 30] + costs[2]
                )

        return dp[1]