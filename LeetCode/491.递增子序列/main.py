#!/usr/bin/env python
from typing import List
from functools import lru_cache as cache

import bisect
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)

        @cache
        def dfs(pos, stack):
            if pos == n: return

            orig = stack
            num = nums[pos]

            # 选用num的情况
            tgt_pos = bisect.bisect(stack, num)
            stack = stack[:tgt_pos] + (num,)
            if len(stack) > 1: ans.add(stack)
            dfs(pos + 1, stack)

            # 不选用num的情况
            dfs(pos + 1, orig)

        dfs(0, ())
        return list(ans)