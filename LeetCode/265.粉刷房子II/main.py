#!/usr/bin/env python

from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        F = float('inf')
        n, k = len(costs), len(costs[0])
        dp = [[F for _ in range(k)] for _ in range(n)]

        dp[0] = costs[0][:]
        min_cost, min_cost_i, sec_min_cost = F, -1, F
        for i, cost in enumerate(costs[0]):
            if cost < min_cost:
                sec_min_cost = min_cost
                min_cost, min_cost_i = cost, i
            elif cost < sec_min_cost:
                sec_min_cost = cost

        for i in range(1, n):
            row_min_cost, row_min_cost_i, row_sec_min_cost = F, -1, F
            for j in range(k):
                baseline = min_cost if j != min_cost_i else sec_min_cost
                dp[i][j] = min(dp[i][j], costs[i][j] + baseline)

                if dp[i][j] < row_min_cost:
                    row_sec_min_cost = row_min_cost
                    row_min_cost, row_min_cost_i = dp[i][j], j
                elif dp[i][j] < row_sec_min_cost:
                    row_sec_min_cost = dp[i][j]

            min_cost, min_cost_i, sec_min_cost = row_min_cost, row_min_cost_i, row_sec_min_cost

        return min_cost