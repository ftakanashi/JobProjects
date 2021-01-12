#!/usr/bin/env python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(choices: List[int], start: int):
            s = sum(choices)
            for i in range(start, n):

                # 和39题第二个不同：为了避免重复的几套结果，对于探索中非位于start的重复元素全部跳过
                if i > start and candidates[i-1] == candidates[i]:
                    continue

                cand = candidates[i]
                if s + cand == target:
                    res.append(choices + [cand,])
                    return
                elif s + cand > target:
                    return
                else:
                    dfs(choices + [cand,], i + 1)    # 和39题第一个不同，递归进入时start是i + 1

        dfs([], 0)
        return res