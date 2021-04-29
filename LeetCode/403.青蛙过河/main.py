#!/usr/bin/env python

from typing import List

from functools import lru_cache as cache

class Solution1:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        dp = [set() for _ in range(len(stones))]
        dp[0].add(0)
        dp[1].add(1)
        for i in range(2, len(stones)):
            for j in range(1, i):
                diff = stones[i] - stones[j]
                if diff - 1 in dp[j] or diff in dp[j] or diff + 1 in dp[j]:
                    dp[i].add(diff)

        return len(dp[-1]) > 0

class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        n = len(stones)
        stone2i = {s: i for i, s in enumerate(stones)}

        @cache
        def dfs(start, dist):
            if start == n - 1: return True
            s = stones[start]
            for nxt_s in (dist - 1, dist, dist + 1):
                if nxt_s <= 0: continue
                if s + nxt_s in stone2i:
                    if dfs(stone2i[s+nxt_s], nxt_s): return True
            return False

        return dfs(1, 1)
