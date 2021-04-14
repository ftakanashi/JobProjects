#!/usr/bin/env python
from typing import List

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        states = [0 for _ in range(numCourses)]

        def dfs(node):
            states[node] = 1
            for e in graph[node]:
                if states[e] == 1 or (states[e] == 0 and not dfs(e)): return False
            states[node] = 2
            return True

        for i in range(numCourses):
            if states[i] == 0 and not dfs(i): return False

        return True