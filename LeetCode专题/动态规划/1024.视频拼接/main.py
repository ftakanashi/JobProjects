#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:

        dp = [0] + [float('inf')] * T

        for i in range(1, T + 1):

            # 寻找所有aj < i <= bj的子区间[aj, bj]中，使得dp[aj] + 1最小的值
            min_aj = float('inf')
            for aj, bj in clips:
                if aj < i <= bj:
                    min_aj = min(min_aj, dp[aj] + 1)

            # 如果经过状态转移后仍然是inf，则early stopping
            if min_aj == float('inf'):
                return -1
            dp[i] = min_aj    # 更新状态

        return dp[T]