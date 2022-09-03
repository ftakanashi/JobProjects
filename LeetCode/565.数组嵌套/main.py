#!/usr/bin/env python
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        def dfs(pos, link):
            if nums[pos] in link: return len(link)
            seen.add(pos)
            link.add(nums[pos])
            return dfs(nums[pos], link)

        n = len(nums)
        ans = 0
        for i in range(n):
            if i in seen: continue
            tmp = set()
            ans = max(ans, dfs(i, tmp))
        return ans