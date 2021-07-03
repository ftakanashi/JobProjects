#!/usr/bin/env python
from typing import List

from functools import lru_cache as cache

class Solution1:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(bikes), len(workers)

        def get_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # 过多参数版本的dfs，能AC但效率很差
        # @cache
        # def dfs(start, total_dist, mask):
        #     if start == n: return total_dist
        #     worker = workers[start]
        #     ans = float('inf')
        #     for j in range(m):
        #         if (mask >> j) & 1 == 1: continue
        #         mask = mask | (1 << j)
        #         ans = min( ans, dfs(start + 1, total_dist + get_dist(worker, bikes[j]), mask) )
        #         mask = mask ^ (1 << j)
        #     return ans
        #
        # return dfs(0, 0, 0)

        @cache
        def dfs(start, mask):
            if start == n: return 0
            worker = workers[start]
            ans = float('inf')
            for j in range(m):
                if (mask >> j) & 1 == 1: continue
                # mask = mask | (1 << j)
                # ans = min( ans, dfs(start + 1, mask) + get_dist(worker, bikes[j]))
                # mask = mask ^ (1 << j)
                # 找理由回溯法的mask应该像如上操作。但显然，这三行和下面一行是等价的
                ans = min( ans, dfs( start + 1, mask | (1<<j) ) + get_dist(worker, bikes[j]))
            return ans

        return dfs(0, 0)