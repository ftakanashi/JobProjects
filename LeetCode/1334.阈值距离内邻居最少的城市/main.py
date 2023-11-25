#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import copy
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        F = float("inf")
        path = [[F for _ in range(n)] for _ in range(n)]
        for x, y, val in edges:
            path[x][y] = path[y][x] = val

        # floyd算法
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if path[i][k] + path[k][j] < path[i][j]:
                        path[i][j] = path[i][k] + path[k][j]

        # 对城市的符合条件的邻居数进行计数
        connected = [0 for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if path[i][j] <= distanceThreshold:
                    connected[i] += 1
                    connected[j] += 1

        # 排序并返回答案
        for _, ans in sorted([(c, -i) for i, c in enumerate(connected)]):
            return -ans