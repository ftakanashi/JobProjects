#!/usr/bin/env python

from typing import List

F = float('inf')
class Item:
    def __init__(self):
        self.min_val = F
        self.min_i = -1
        self.sec_min_val = F

    def update(self, j_ind, val):
        if val < self.min_val:
            self.sec_min_val = self.min_val
            self.min_val = val
            self.min_i = j_ind
        elif val < self.sec_min_val:    # !!! 别忘了这个逻辑 如果新进来的值不急min_val小，但是比sec_min_val小的话也要更新 !!!
            self.sec_min_val = val

    def get(self, j_ind):
        return self.min_val if j_ind != self.min_i else self.sec_min_val

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        dp = [[[F for _ in range(target + 1)] for _ in range(n + 1)] for _ in range(m)]
        if houses[0] == 0:
            for j in range(1, n+1): dp[0][j][1] = cost[0][j - 1]
        else:
            c = houses[0]
            dp[0][c][1] = 0

        mem = [[Item() for _ in range(target + 1)] for _ in range(m)]
        # 别忘了基于最初的DP值对mem进行初始化
        for j in range(1, n + 1):
            for k in range(1, target + 1):
                mem[0][k].update(j, dp[0][j][k])

        for i in range(1, m):
            c = houses[i]
            for j in range(1, n + 1):
                if c != 0 and j != c: continue
                this_cost = cost[i][j-1] if c == 0 else 0
                for k in range(1, target + 1):
                    v = min(mem[i-1][k-1].get(j), dp[i-1][j][k]) + this_cost
                    dp[i][j][k] = v
                    mem[i][k].update(j, v)

        res = mem[m-1][target].min_val
        return res if res < F else -1

        # 以下是没有优化的 纯三维DP 的代码
        # for i in range(1, m):
        #     c = houses[i]
        #     for j in range(1, n+1):
        #         if c != 0 and j != c: continue
        #         this_cost = cost[i][j-1] if c == 0 else 0
        #         for k in range(1, target + 1):
        #             v = min(dp[i-1][x][k-1] for x in range(1, n+1) if x != j)
        #             v = min(v, dp[i-1][j][k])
        #             dp[i][j][k] = v + this_cost

        # res = F
        # for j in range(1, n+1):
        #     res = min(res, dp[m-1][j][target])
        # return res if res < F else -1