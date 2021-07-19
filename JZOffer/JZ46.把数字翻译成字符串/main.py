#!/usr/bin/env python
from functools import lru_cache as cache
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)

        @cache
        def dfs(start: int) -> int:
            if start >= n: return 1
            count = 0
            count += dfs(start + 1)
            if num[start] != '0' and start + 1 < n and int(num[start:start+2]) < 26:
                count += dfs(start + 2)
            return count

        return dfs(0)