#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        organization = defaultdict(set)
        for me, leader in enumerate(manager):
            organization[leader].add(me)

        queue = deque()
        queue.append((headID, 0))
        ans = 0
        while queue:
            node, time = queue.popleft()
            ans = max(ans, time)
            for nxt in organization[node]:
                queue.append((nxt, time + informTime[node]))
        return ans