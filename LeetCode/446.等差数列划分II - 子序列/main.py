#!/usr/bin/env python
from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:    # 因为默认值也是0，所以这个判断其实可以不要。
                    ans += dp[j][diff]
                dp[i][diff] += (dp[j][diff] + 1)
        return ans