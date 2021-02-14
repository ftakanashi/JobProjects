#!/usr/bin/env python
from typing import List

class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(ans, seen):
            if len(ans) == n:
                res.append(ans)
                return
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    dfs(ans+[num,], seen)
                    seen.remove(num)
        dfs([], set([]))
        return res

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(pos: int):
            if pos == n - 1:
                res.append(nums.copy())
                return
            for i in range(pos, n):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        dfs(0)
        return res