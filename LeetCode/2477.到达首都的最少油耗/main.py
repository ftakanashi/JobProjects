#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        # 首先构建图
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        ans = 0

        def dfs(node, parent):
            nonlocal ans
            people = 1
            for nxt in graph[node]:
                if nxt == parent: continue    # 防止走回头路
                people += dfs(nxt, node)
            if node > 0:    # 加这个判断的主要原因是如果不加，会额外算上从0号节点出发的额外油耗，但是实际上并不存在这部分油耗
                ans += (math.ceil(people / seats))    # 别忘了这里除不尽的话要向上取整
            return people

        dfs(0, None)
        return ans