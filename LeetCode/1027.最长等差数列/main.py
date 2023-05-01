#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(lambda: 1) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j][d] + 1

        return max([max(cnt.values()) for cnt in dp])