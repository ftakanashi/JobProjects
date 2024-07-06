#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import defaultdict
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:

        # 构建图
        graph = defaultdict(list)
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))

        # dfs函数。为了避免走回头路，将parent作为参数传递
        def dfs(parent, node, dist):
            cnt = 1 if dist % signalSpeed == 0 else 0
            for child, weight in graph[node]:
                if child == parent: continue
                cnt += dfs(node, child, dist + weight)
            return cnt

        ans = [0 for _ in range(len(edges) + 1)]    # 虽然题目没给出n，但是别忘了树的边加一就是节点数
        for node in graph:
            # 求算每个节点作为根节点时，其所有子树的可达节点数
            child_cnts = [dfs(node, c, w) for c, w in graph[node]]
            # 两两相乘
            for i in range(len(child_cnts)):
                for j in range(i):
                    ans[node] += child_cnts[i] * child_cnts[j]
        return ans