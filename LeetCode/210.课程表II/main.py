#!/usr/bin/env python
from typing import List

import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 将给出的数据转换成邻接表的形式
        graph = collections.defaultdict(list)
        for p, a in prerequisites:
            graph[a].append(p)

        # 这里实现上没有采用状态数组，而是用了两个哈希集。
        # visited 保存已经经历第二状态的节点
        # finished 保存已经经历第三状态的节点
        res = []
        visited = set()
        finished = set()

        def dfs(node):
            visited.add(node)
            for e in graph[node]:
                if e in finished: continue    # 下游节点已经处于第三状态的情况
                if e in visited or not dfs(e): return False    # 本层或者下层递归发现环时
            res.append(node)    # 收割结果
            finished.add(node)
            return True

        for i in range(numCourses):
            if i not in finished and i not in visited:
                flag = dfs(i)
                if not flag: return []

        res.reverse()
        return res