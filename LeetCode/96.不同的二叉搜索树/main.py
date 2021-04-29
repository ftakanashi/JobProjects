#!/usr/bin/env python

from functools import lru_cache as cache

class Solution1:
    def numTrees(self, n: int) -> int:

        @cache
        def dfs(s: int, e: int) -> int:
            if s >= e: return 1
            cnt = 0
            for i in range(s, e + 1):
                l_pats = dfs(s, i - 1)
                r_pats = dfs(i + 1, e)
                cnt += (l_pats * r_pats)

            return cnt

        return dfs(1, n)

class Solution2:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for k in range(1, i+1):
                dp[i] += dp[k-1] * dp[i-k]
        return dp[-1]