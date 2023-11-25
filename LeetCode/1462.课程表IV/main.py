#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import copy
from collections import defaultdict
from functools import lru_cache as cache

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        # 构建图
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[a].add(b)

        # 维护后辈节点的数据结构
        ascendants = defaultdict(set)

        @cache
        def dfs(node):
            ascendants[node] = copy.copy(graph[node])
            for nxt in graph[node]:
                ascendants[node] = ascendants[node].union(dfs(nxt))   # 取并集
            return ascendants[node]

        for i in range(numCourses):
            dfs(i)    # 因为不知道图的顶端节点是谁，所以只能全部来一遍。由于有记忆化，所以实际并没有特别大损耗

        return [b in ascendants[a] for a, b in queries]