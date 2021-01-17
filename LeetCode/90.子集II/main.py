#!/usr/bin/env python
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        total_res = []

        def dfs(start: int, res: List[int]):
            total_res.append(res)
            if start >= n: return
            i = start
            prev = None
            while i < n:
                if nums[i] != prev:
                    dfs(i + 1, res + [nums[i], ])
                    prev = nums[i]
                i += 1

        dfs(0, [])
        return total_res