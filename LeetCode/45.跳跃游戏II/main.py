#!/usr/bin/env python
from typing import List

class Solution1:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] + [float('inf') for _ in range(n-1)]
        i = 0
        edge = 1    # 初始化某个位置探索到的最远边界
        while i < n:
            j = edge
            while j < n and j <= i + nums[i]:
                dp[j] = dp[i] + 1
                j += 1
            edge = max(edge, nums[i] + i + 1)    # 考虑到nums[i] + i + 1小于当前edge的情况，因此使用max而不是直接用nums[i]+i+1
            if j == n:
                break
            i += 1
        return dp[-1]

class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step