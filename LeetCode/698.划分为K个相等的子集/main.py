#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from functools import lru_cache as cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        mean = sum(nums) / k
        if mean != int(mean): return False
        mean = int(mean)
        for num in nums:
            if num > mean: return False

        n = len(nums)

        @cache
        def dfs(curr, used):
            if used == 2 ** n - 1:
                return curr == mean

            for i, num in enumerate(nums):
                if used & (1 << i) > 0: continue
                new_used = used | (1 << i)
                if curr == mean and dfs(num, new_used):
                    return True
                elif curr + num <= mean and dfs(curr + num, new_used):
                    return True

            return False

        return dfs(0, 0)

