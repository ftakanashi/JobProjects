#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mp = defaultdict(list)
        row = [0] * m
        col = [0] * n

        # 记录 mat值 -> 坐标列表 的映射
        for i in range(m):
            for j in range(n):
                mp[mat[i][j]].append((i, j))

        # 从小到大遍历所有值。但是值本身并不需要关心，因此用 _ 表示即可
        for _, pos in sorted(mp.items(), key=lambda x: x[0):
            # 要走到当前值对应的这些格子，需要的最大步数。由于可能有多个格子，所以输出的是一个列表
            # 遍历过程中 rows 和 cols 会有大量0的位置，表示从对应行/列没有合适的位置可以走到当前格子
            res = [max(row[i], col[j]) + 1 for i, j in pos]

            # 针对某一个当前值的格子，针对其所在行/列，更新 rows 和 cols
            for (i, j), d in zip(pos, res):
                row[i] = max(row[i], d)
                col[j] = max(col[j], d)

        # 最后结果可以是 max(row) 或者 max(col)
        return max(row)