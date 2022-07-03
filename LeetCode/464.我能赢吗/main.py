#!/usr/bin/env python
from functools import lru_cache as cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger + 1) // 2:
            return False

        @cache
        def dfs(used, total):
            for num in range(1, maxChoosableInteger + 1):
                if ((1 << num) & used) > 0: continue
                if total + num >= desiredTotal or not dfs(used | (1 << num), total + num):
                    return True
            return False

        return dfs(0, 0)