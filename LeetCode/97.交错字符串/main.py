#!/usr/bin/env python
from functools import lru_cache as cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == '': return s2 == s3
        if s2 == '': return s1 == s3
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False

        @cache
        def dfs(i, j, k):
            if i == n1: return s2[j:] == s3[k:]
            if j == n2: return s1[i:] == s3[k:]
            if s1[i] == s3[k] or s2[j] == s3[k]:
                flag = False
                if s1[i] == s3[k]:
                    flag = flag or dfs(i+1, j, k+1)
                if s2[j] == s3[k]:
                    flag = flag or dfs(i, j+1, k+1)
                return flag

            else:
                return False

        return dfs(0, 0, 0)