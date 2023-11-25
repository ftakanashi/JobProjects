#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import defaultdict
from functools import lru_cache as cache

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prev = defaultdict(set)
        for a, b in relations:
            prev[b].add(a)

        @cache
        def dfs(node):
            t = 0
            for p in prev[node]:
                t = max(t, dfs(p))
            t += time[node - 1]
            return t

        ans = 0
        for i in range(1, n + 1):
            ans = max(ans, dfs(i))
        return ans