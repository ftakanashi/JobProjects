#!/usr/bin/env python

from typing import List
from functools import lru_cache as cache

class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @cache
        def dfs(rest):
            if rest == 0: return 1
            if rest < 0: return 0
            cnt = 0
            for n in nums:
                cnt += dfs(rest - n)
                if n > rest: break
            return cnt

        return dfs(target)

class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = set(nums)
        dp = [1 if i in nums else 0 for i in range(target + 1)]

        for j in range(1, target + 1):
            for i in range(j):
                if (j - i) in nums:
                    dp[j] += dp[i]

        return dp[-1]