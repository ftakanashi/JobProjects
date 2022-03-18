#!/usr/bin/env python
from typing import List

from functools import reduce, lru_cache as cache
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = reduce(lambda a,b:a|b, nums)
        nums.sort(reverse=True)
        n = len(nums)

        @cache
        def dfs(pos, curr):
            if pos == n:
                return 1 if curr == target else 0
            if curr == target:
                return 2 ** (n - 1 - pos + 1)

            return dfs(pos + 1, curr) + dfs(pos + 1, curr | nums[pos])

        return dfs(0, 0)