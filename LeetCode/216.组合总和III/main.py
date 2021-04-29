#!/usr/bin/env python

from typing import List
from functools import lru_cache as cache

class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        @cache
        def dfs(rest_k, rest_n, path):
            if rest_k == 0:
                if rest_n == 0: res.append(path)
                return

            num = path[-1] + 1 if path else 1
            while num < 10:
                if num > rest_n: break
                dfs(rest_k - 1, rest_n - num, path + (num,))
                num += 1

        dfs(k, n, ())
        return res

class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [[ [] for _ in range(n + 1)] for _ in range(10)]

        for i in range(1, 10):
            for j in range(1, n + 1):
                container = dp[i][j]
                container.extend(dp[i-1][j])
                if j - i == 0 or (j - i > 0 and len(dp[i-1][j-i]) > 0):
                    if j - i == 0:
                        container.append((i, ))
                    else:
                        container.extend(l + (i,) for l in dp[i-1][j-i])

        return [l for l in dp[-1][-1] if len(l) == k]