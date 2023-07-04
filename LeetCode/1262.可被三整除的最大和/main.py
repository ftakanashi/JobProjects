#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        r1, r2, r3 = [], [], []
        for num in nums:
            if num % 3 == 0:
                r1.append(num)
            elif num % 3 == 1:
                r2.append(num)
            else:
                r3.append(num)

        # 为了最终和尽量大，应该先行排序
        r2.sort(reverse=True)
        r3.sort(reverse=True)

        ans = 0
        l2, l3 = len(r2), len(r3)
        for v2 in [l2 - 2, l2 - 1, l2]:
            if v2 < 0: continue    # 兼容r2以及r3本身长度不到3的情况
            for v3 in [l3 - 2, l3 - 1, l3]:
                if v3 < 0: continue
                tmp = sum(r2[:v2]) + sum(r3[:v3])
                if tmp % 3 == 0:
                    ans = max(ans, tmp)

        return ans + sum(r1)

class Solution2:
    def maxSumDivThree(self, nums: List[int]) -> int:
        INF = float("-inf")
        dp = [0, INF, INF]

        for num in nums:
            new_dp = dp.copy()    # 状态压缩
            for i in range(3):
                # 核心状态转移方程，下标对应关系的归纳式是最核心的
                new_dp[(i + num % 3) % 3] = max(new_dp[(i + num % 3) % 3], dp[i] + num)
            dp = new_dp

        return dp[0]