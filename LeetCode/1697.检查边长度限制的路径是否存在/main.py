#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # 极简并查集模板
        fa = [_i for _i in range(n)]
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(x, y):
            fa[find(x)] = find(y)

        i = 0
        ans = [False for _ in range(len(queries))]    # 答案数组要全量初始化，因为后面query会打乱排序，所以要按图索骥
        edgeList.sort(key=lambda e: e[2])    # 将所有边按照权值从小到大排序

        # 按limit从小到大遍历所有query
        for j, (x, y, limit) in sorted(enumerate(queries), key=lambda q: q[1][2]):

            # 将边权值小于当前limit的所有边都加入并查集
            while i < len(edgeList) and edgeList[i][2] < limit:
                merge(edgeList[i][0], edgeList[i][1])
                i += 1

            ans[j] = find(x) == find(y)    # 判断query中的两个节点在当前的图（保证所有边权值都小于limit）中是否处于同一个联通分量

        return ans