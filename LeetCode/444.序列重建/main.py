#!/usr/bin/env python
from typing import List

from collections import defaultdict, deque
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 构建图，统计入度数组
        graph = defaultdict(list)
        in_deg = [0 for _ in range(len(nums) + 1)]
        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].append(seq[i])
                in_deg[seq[i]] += 1

        q = deque([i for i, d in enumerate(in_deg) if i > 0 and d == 0])    # 队列中始终维护当前遍历时入度为0的节点

        while q:
            if len(q) > 1: return False
            node = q.popleft()
            for nxt in graph[node]:
                in_deg[nxt] -= 1    # 别忘了及时更新入度
                if in_deg[nxt] == 0:
                    q.append(nxt)
        return True