#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        other = {0: (1, 2), 1: (0, 2), 2: (0, 1)}

        dp = [1, 0, 1]
        for i in range(1, n):
            new_dp = [float('inf')] * 3
            for j in range(3):
                if obstacles[i - 1] - 1 != j:
                    new_dp[j] = min(new_dp[j], dp[j])
                for o in other[j]:
                    if obstacles[i] - 1 == o:
                        continue
                    new_dp[j] = min(new_dp[j], dp[o] + 1)

                if obstacles[i] > 0:
                    new_dp[obstacles[i] - 1] = float('inf')

            dp = new_dp

        return min(dp)