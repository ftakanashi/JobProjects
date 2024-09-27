#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0
        opened = [0] * n
        f = lambda x: opened[x] > 0
        for mask in range(1 << n):  # 一种新的遍历所有子集的办法

            # 构建当前mask下的opened数组，用于后续方便地快速知道某个节点是否被关闭了
            for i in range(n):
                opened[i] = mask & (1 << i)

            # 距离数组，size为 n*n
            d = [[1000000] * n for i in range(n)]
            # 初始化距离数组
            for i, j, r in roads:
                if opened[i] == 0 or opened[j] == 0: continue
                d[i][j] = d[j][i] = min(d[i][j], d[j][i], r)

            # floyd
            for k in filter(f, range(n)):
                for i in filter(f, range(n)):
                    for j in filter(f, range(i + 1, n)):
                        d[i][j] = d[j][i] = min(d[i][j], d[i][k] + d[k][j])

            def calc():
                # 遍历当前所有开放节点的pair，看其距离是否超过要求的最大值，若是则直接放弃这种可能
                # 若否，则说明当前方案是可行的，可以 += 1
                for i in filter(f, range(n)):
                    for j in filter(f, range(i + 1, n)):
                        if d[i][j] > maxDistance:
                            return 0
                return 1

            ans += calc()

        return ans