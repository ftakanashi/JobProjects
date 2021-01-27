#!/usr/bin/env python
from typing import List

class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        mem = {}
        def dfs(res: int, start: int) -> int:
            if (res, start) in mem: return mem[(res, start)]
            if start == len(nums):
                if res == S:
                    return 1
                return 0

            n = nums[start]
            count = dfs(res + n, start + 1) + dfs(res - n, start + 1)
            mem[(res, start)] = count
            return count

        return dfs(0, 0)

class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [[0 for _ in range(2001)] for _ in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1    # 考虑到nums[0] == 0的情况
        for i in range(1, len(nums)):
            n = nums[i]
            for j in range(-1000, 1000):
                if dp[i - 1][j + 1000] > 0:
                    dp[i][j + 1000 + n] += dp[i - 1][j + 1000]
                    dp[i][j + 1000 - n] += dp[i - 1][j + 1000]

        return dp[len(nums) - 1][S + 1000] if -1000 <= S <= 1000 else 0