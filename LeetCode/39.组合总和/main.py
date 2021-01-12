#!/usr/bin/env python

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(start: int, choices: List[int]):
            s = sum(choices)
            for i in range(start, n):
                cand = candidates[i]
                if s + cand > target:
                    return
                elif s + cand == target:
                    res.append(choices + [cand,])
                    return
                else:
                    dfs(i, choices + [cand,])

        dfs(0, [])
        return res