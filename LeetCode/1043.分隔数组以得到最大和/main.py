#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n: return max(arr) * n
        dp = [0 for _ in range(n)]

        # 填充前k个位置的DP值，方便后面计算
        tmp = float("-inf")
        for i in range(k):
            tmp = max(tmp, arr[i])
            dp[i] = (i + 1) * tmp

        for i in range(k, n):
            max_v = arr[i]
            # 在每一个i开始遍历后，对j的遍历可以倒序进行，这样一次遍历中就可以始终维护到当前j到i之间的最大值
            for j in range(i - 1, i - k - 1, -1):
                dp[i] = max(dp[i], dp[j] + (i - j) * max_v)
                max_v = max(max_v, arr[j])

        return dp[-1]