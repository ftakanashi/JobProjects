#!/usr/bin/env python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_res = []

        def dfs(start: int, res: List[int]):
            total_res.append(res)
            if start == n: return
            for i in range(start, n):
                dfs(i + 1, res + [nums[i], ])

        dfs(0, [])
        return total_res