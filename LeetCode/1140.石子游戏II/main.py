#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from functools import lru_cache as cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        post_sum = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            post_sum[i] = post_sum[i + 1] + piles[i]

        @cache
        def dfs(i, M):
            if i >= n: return 0
            if i + M * 2 >= n: return post_sum[i]
            ans = 0
            for x in range(1, M * 2 + 1):
                # 下面这行最关键，我当前选择的x，应该让对手在下一轮尽可能少收益，这才是最优策略
                ans = max(ans, post_sum[i] - dfs(i + x, max(x, M)))
            return ans

        return dfs(0, 1)