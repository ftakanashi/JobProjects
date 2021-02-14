#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def generateMap(self, cols):
        res_map = []
        n = len(cols)
        for i in range(n):
            checks = ['.' for _ in range(n)]
            checks[cols[i]] = 'Q'
            res_map.append(''.join(checks))
        return res_map

    def solveNQueens(self, n: int) -> List[List[str]]:
        all_res = []
        col = set()
        diff_diag = set()
        sum_diag = set()

        def dfs(res: List[int]):
            if len(res) == n:
                all_res.append(res.copy())
                return
            i = len(res)
            for j in range(n):
                if j in col or (i-j) in diff_diag or (i+j) in sum_diag: continue
                col.add(j)
                diff_diag.add(i - j)
                sum_diag.add(i + j)
                res.append(j)
                dfs(res)
                col.remove(j)
                diff_diag.remove(i - j)
                sum_diag.remove(i + j)
                res.pop()

        dfs([])
        for i, res in enumerate(all_res):
            all_res[i] = self.generateMap(res)
        return all_res