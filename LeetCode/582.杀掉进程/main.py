#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for child, parent in zip(pid, ppid):
            graph[parent].append(child)
        ans = []

        def dfs(pid):
            ans.append(pid)
            for child in graph[pid]:
                dfs(child)

        dfs(kill)
        return ans