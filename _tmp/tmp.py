#!/usr/bin/env python
from typing import List
from functools import lru_cache as cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def dfs(i, j, path):
            if i == n: return path
            ans = max(
                dfs(i+1, j, path + triangle[i][j]),
                dfs(i+1, j+1, path + triangle[i][j])
            )
            return ans

        return dfs(0, 0, 0)

if __name__ == '__main__':
    s = Solution()
    res = s.minimumTotal([[2,], [3,4]])
    print(res)