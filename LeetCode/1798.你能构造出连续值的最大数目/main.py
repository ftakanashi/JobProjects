#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        if coins[0] > 1:    # 如果最小的硬币都大于1的话，直接返回1即可，这是一个需要特殊处理的特殊情况
            return 1

        ans = 2
        for i in range(1, n):
            coin = coins[i]
            if coin <= ans:
                ans = coin + ans
            else:
                break
        return ans