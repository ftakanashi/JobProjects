#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        # 一次遍历，将每个子数组对应的各自的最大值保存在 max_v 数组中
        max_v = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            m = arr[i]
            for j in range(i, n):
                m = max(m, arr[j])
                max_v[i][j] = m

        # 初始化DP数组，对角线全是代表单个叶子节点，因此代价值全为0
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        # 正式DP遍历，注意遍历的具体顺序和方向
        for j in range(n):
            for i in range(j - 1, -1, -1):
                for k in range(i, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k + 1][j] + max_v[i][k] * max_v[k + 1][j]
                    )

        return dp[0][n - 1]