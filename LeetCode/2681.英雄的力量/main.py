#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        dp = [0 for _ in range(len(nums))]
        s = ans = 0

        for i, num in enumerate(nums):
            dp[i] = (s + num) % MOD
            ans = (ans + num * num * dp[i]) % MOD
            s = (s + dp[i]) % MOD

        return ans