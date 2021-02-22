#!/usr/bin/env python
from typing import List

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        e = sum(nums) // 4
        if sum(nums) % e != 0 or len(nums) < 4: return False

        nums.sort(reverse=True)
        edges = [0, 0, 0, 0]
        def dfs(start: int) -> bool:
            if start == len(nums):
                return edges[0] == edges[1] == edges[2] == edges[3] == e
            for i in range(4):
                if edges[i] + nums[start] <= e:
                    edges[i] += nums[start]
                    if dfs(start + 1): return True
                    edges[i] -= nums[start]    # 回溯
            return False
        return dfs(0)