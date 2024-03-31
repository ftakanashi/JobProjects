#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # 构建图，构建edges哈希集
        graph = collections.defaultdict(set)
        edges = set([(a, b) for a, b in connections])
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        ans = 0
        seen = set()

        def dfs(node):
            nonlocal ans
            seen.add(node)    # 防止重复遍历死循环
            for nxt in graph[node]:
                if nxt in seen: continue
                if (node, nxt) in edges:
                    # 由于是从0向其他节点遍历，所以当某个上层节点指向下层节点的边存在时，说明这是一条需要改方向的边，因此ans += 1
                    ans += 1
                dfs(nxt)

        dfs(0)
        return ans
