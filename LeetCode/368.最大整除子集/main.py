#!/usr/bin/env python

from typing import List
from functools import lru_cache as cache

class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        @cache
        def dfs(start, resmax):
            res = []
            for j in range(start, len(nums)):
                if nums[j] % resmax == 0:
                    tmp = [nums[j],] + dfs(j + 1, nums[j])
                    if len(tmp) > len(res):
                        res = tmp
            return res

        return dfs(0, 1)

class Solution2:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 根据dp数组的值找出一个答案
        i, res, p = n-1, [], max(dp)
        while p > 0 and i >= 0:
            if p == dp[i] and (not res or res[-1] % nums[i] == 0):
                res.append(nums[i])
                p -= 1
            i -= 1
        res.reverse()    # 因为输出是无序集合 不加也没关系，纯粹为了输出好看
        return res