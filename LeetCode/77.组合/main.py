#!/usr/bin/env python
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or k == 0: return []
        if k == n: return [list(range(1, n+1))]
        res = []

        def dfs(comb: List[int], rest_k: int):
            if rest_k == 0:
                res.append(comb)
                return
            start = 1 if len(comb) == 0 else comb[-1] + 1
            for i in range(start, n+1):
                dfs(comb + [i,], rest_k - 1)

        dfs([], k)
        return res